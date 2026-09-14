# NIFTY & BANKNIFTY

Strategy: 60–90 DTE asymmetric Iron Condor planning, following the SPY/QQQ level-map format.

- NIFTY: weekly expiry is Tuesday; use the first available Tuesday expiry that gives approximately 60–90 DTE at entry.
- BANKNIFTY: use the nearest monthly expiry that gives approximately 60–90 DTE at entry. Do **not** assume a weekly BANKNIFTY expiry.
- Preferred structure: asymmetric Iron Condor, bullish bias.
- Target short put: ~10–12 delta.
- Target short call: ~15–18 delta.
- Long wings: ~5–8 delta, sized for defined risk and acceptable credit.
- Normal management: harvest ~40–60% of initial credit; reassess aggressively once ~21–30 DTE remains.
- Avoid forcing a trade when IV/risk premium, expected range, liquidity, or portfolio exposure is unattractive.

## Forward Level Map

| Expiry Week | NIFTY_1 | NIFTY_2 | BANKNIFTY_1 | BANKNIFTY_2 |
|---|---:|---:|---:|---:|
| 2026-09-22 | | | | |
| 2026-09-29 | | | | |
| 2026-10-06 | | | | |
| 2026-10-13 | | | | |
| 2026-10-20 | | | | |
| 2026-10-27 | | | | |
| 2026-11-03 | | | | |
| 2026-11-10 | | | | |
| 2026-11-17 | | | | |
| 2026-11-24 | | | | |
| 2026-12-01 | | | | |
| 2026-12-08 | | | | |
| 2026-12-15 | | | | |
| 2026-12-22 | | | | |
| 2026-12-29 | | | | |
| 2027-01-05 | | | | |
| 2027-01-12 | | | | |
| 2027-01-19 | | | | |
| 2027-01-26 | | | | |
| 2027-02-02 | | | | |
| 2027-02-09 | | | | |
| 2027-02-16 | | | | |
| 2027-02-23 | | | | |
| 2027-03-02 | | | | |
| 2027-03-09 | | | | |
| 2027-03-16 | | | | |
| 2027-03-23 | | | | |
| 2027-03-30 | | | | |
| 2027-04-06 | | | | |
| 2027-04-13 | | | | |
| 2027-04-20 | | | | |
| 2027-04-27 | | | | |
| 2027-05-04 | | | | |
| 2027-05-11 | | | | |
| 2027-05-18 | | | | |
| 2027-05-25 | | | | |
| 2027-06-01 | | | | |
| 2027-06-08 | | | | |
| 2027-06-15 | | | | |
| 2027-06-22 | | | | |
| 2027-06-29 | | | | |
| 2027-07-06 | | | | |
| 2027-07-13 | | | | |
| 2027-07-20 | | | | |
| 2027-07-27 | | | | |
| 2027-08-03 | | | | |
| 2027-08-10 | | | | |
| 2027-08-17 | | | | |
| 2027-08-24 | | | | |
| 2027-08-31 | | | | |
| 2027-09-07 | | | | |
| 2027-09-14 | | | | |
| 2027-09-21 | | | | |
| 2027-09-28 | | | | |
| 2027-10-05 | | | | |
| 2027-10-12 | | | | |
| 2027-10-19 | | | | |
| 2027-10-26 | | | | |
| 2027-11-02 | | | | |
| 2027-11-09 | | | | |
| 2027-11-16 | | | | |
| 2027-11-23 | | | | |
| 2027-11-30 | | | | |
| 2027-12-07 | | | | |
| 2027-12-14 | | | | |
| 2027-12-21 | | | | |
| 2027-12-28 | | | | |

## Notes

- Populate NIFTY_1 / NIFTY_2 and BANKNIFTY_1 / BANKNIFTY_2 with the selected short-strike planning levels for each relevant 60–90 DTE setup.
- Keep the final strike selection delta-based rather than percentage-distance based.
- Terminal planning assumption for the broader thesis: NIFTY 30,000 and BANKNIFTY 71,000 by end-December 2027.
- Tuesday is the expiry anchor for the NIFTY weekly cycle; expiry dates can shift for exchange holidays.
