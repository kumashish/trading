#!/usr/bin/env python3
"""
reads the CSV, fetches actual closes for the previous Friday,
determines which band was hit and writes results back to the CSV.

Requires: pandas, yfinance, python-dateutil
"""

import os
import math
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta, timezone
from dateutil import parser

CSV_PATH = os.environ.get("CSV_PATH", "data/spy_qqq_11_07_25.csv")
TZ_OVERRIDE = os.environ.get("TZ_OVERRIDE")  # optional like "Asia/Kolkata"

def today_date():
    # Use UTC day by default; if TZ_OVERRIDE is provided, convert to that timezone's date
    now = datetime.now(timezone.utc)
    if TZ_OVERRIDE:
        try:
            import pytz
            tz = pytz.timezone(TZ_OVERRIDE)
            now = now.astimezone(tz)
        except Exception:
            # fallback to UTC if pytz not installed / error
            pass
    return now.date()

def target_friday_date():
    # Action runs on Saturday -> we want the Friday before (yesterday)
    d = today_date() - timedelta(days=1)
    return d

def parse_date(cell):
    # Accept strings like '2025-10-31' or 'Oct 31 2025' etc.
    if pd.isna(cell):
        return None
    if isinstance(cell, (datetime, pd.Timestamp)):
        return cell.date()
    try:
        return parser.parse(str(cell)).date()
    except Exception:
        return None

def parse_band(band_str):
    # band_str expected like "620–656" or "620-656" (en dash or hyphen)
    if pd.isna(band_str):
        return None, None
    s = str(band_str).replace('–', '-').replace('—', '-')
    parts = s.split('-')
    try:
        low = float(parts[0])
        high = float(parts[1])
        return low, high
    except Exception:
        return None, None

def fetch_close(ticker, date_obj):
    # yfinance expects period or start/end; fetch that single date's close
    start = date_obj.strftime("%Y-%m-%d")
    end_dt = date_obj + timedelta(days=1)
    end = end_dt.strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start, end=end, progress=False, threads=False)
    if data is None or data.empty:
        return None
    # Use the 'Close' of the trading day
    # If multiple rows (shouldn't be), take the last row
    return float(data['Close'].iloc[-1])

def classify(price, low2, low1, high1, high2):
    # returns band label string
    if price is None:
        return "NoPrice"
    # boundaries inclusive: price <= low2 -> Below -2σ
    if price <= low2:
        return "Below -2σ"
    if low2 < price <= low1:
        return "-2σ to -1σ"
    if low1 < price <= high1:
        return "-1σ to +1σ"
    if high1 < price <= high2:
        return "+1σ to +2σ"
    return "Above +2σ"

def main():
    if not os.path.exists(CSV_PATH):
        raise SystemExit(f"CSV not found at {CSV_PATH}")

    df = pd.read_csv(CSV_PATH, dtype=str)  # read as strings to preserve band formatting

    target = target_friday_date()
    print(f"Target Friday date: {target.isoformat()}")

    # Find row index where the Friday Date matches target
    date_col_candidates = [c for c in df.columns if 'date' in c.lower()]
    if not date_col_candidates:
        raise SystemExit("No date-like column found in CSV (expected a column named 'Friday Date' or similar).")
    date_col = date_col_candidates[0]

    # normalize and find row
    df['_parsed_date'] = df[date_col].apply(parse_date)
    mask = df['_parsed_date'] == target
    if not mask.any():
        print("No row for the target Friday found in CSV. Exiting.")
        return

    idx = df[mask].index[0]
    print(f"Found row index {idx} for date {target}")

    # Tick mapping (assumes columns named 'SPY Base' and band columns like 'SPY ±1σ Band')
    def get_bands(prefix):
        # read the base and bands from the row
        base_col = f"{prefix} Base"
        one_col = f"{prefix} ±1σ Band"
        two_col = f"{prefix} ±2σ Band"
        base_val = df.at[idx, base_col] if base_col in df.columns else None
        one_val = df.at[idx, one_col] if one_col in df.columns else None
        two_val = df.at[idx, two_col] if two_col in df.columns else None
        return base_val, one_val, two_val

    # Get bands for SPY and QQQ
    spy_base, spy_1, spy_2 = get_bands("SPY")
    qqq_base, qqq_1, qqq_2 = get_bands("QQQ")

    # Parse numeric bounds:
    # For ±1σ band we expect "low–high". For ±2σ likewise.
    spy_low1, spy_high1 = parse_band(spy_1)
    spy_low2, spy_high2 = parse_band(spy_2)
    qqq_low1, qqq_high1 = parse_band(qqq_1)
    qqq_low2, qqq_high2 = parse_band(qqq_2)

    # If ±1σ band exists, compute low2/high2 fallback if not directly available:
    # But we expect ±2σ to be present (from the generation code).
    # Fetch actual closes
    spy_close = fetch_close("SPY", target)
    qqq_close = fetch_close("QQQ", target)
    print(f"SPY close: {spy_close}, QQQ close: {qqq_close}")

    # If parsing bands failed, attempt to compute using base and weekly sigma heuristics would be possible,
    # but here we will abort if necessary bands are missing.
    missing = []
    if any(v is None for v in [spy_low1, spy_high1, spy_low2, spy_high2]):
        missing.append("SPY bands")
    if any(v is None for v in [qqq_low1, qqq_high1, qqq_low2, qqq_high2]):
        missing.append("QQQ bands")
    if missing:
        print("Warning: missing band parsing for:", missing)
        # we will still write close price and 'NoBand' label
    # classify
    spy_label = classify(spy_close,
                         spy_low2 if spy_low2 is not None else float('-inf'),
                         spy_low1 if spy_low1 is not None else float('-inf'),
                         spy_high1 if spy_high1 is not None else float('inf'),
                         spy_high2 if spy_high2 is not None else float('inf'))
    qqq_label = classify(qqq_close,
                         qqq_low2 if qqq_low2 is not None else float('-inf'),
                         qqq_low1 if qqq_low1 is not None else float('-inf'),
                         qqq_high1 if qqq_high1 is not None else float('inf'),
                         qqq_high2 if qqq_high2 is not None else float('inf'))

    # Write results into df
    df.at[idx, "SPY_Close"] = spy_close if spy_close is not None else ""
    df.at[idx, "SPY_Hit_Band"] = spy_label
    df.at[idx, "QQQ_Close"] = qqq_close if qqq_close is not None else ""
    df.at[idx, "QQQ_Hit_Band"] = qqq_label

    # drop helper column
    df = df.drop(columns=['_parsed_date'])

    # Save CSV (preserve original formatting, index=False)
    df.to_csv(CSV_PATH, index=False)
    print(f"Updated {CSV_PATH} and set SPY_Hit_Band={spy_label}, QQQ_Hit_Band={qqq_label}")

if __name__ == "__main__":
    main()
