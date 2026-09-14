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

The columns below are **planning levels for the short strikes**: `_1` = short put and `_2` = short call. They are derived from the assumed path toward NIFTY 30,000 and BANKNIFTY 71,000 by end-December 2027, with a bullish asymmetric buffer. Final strikes must still be selected from live option deltas/IV when the trade is opened.

| Expiry Week | NIFTY_1 | NIFTY_2 | BANKNIFTY_1 | BANKNIFTY_2 |
|---|---:|---:|---:|---:|
| 2026-09-22 | 22400 | 26050 | 51400 | 60400 |
| 2026-09-29 | 22450 | 26100 | 51600 | 60600 |
| 2026-10-06 | 22550 | 26200 | 51700 | 60800 |
| 2026-10-13 | 22600 | 26300 | 51900 | 61100 |
| 2026-10-20 | 22650 | 26350 | 52100 | 61300 |
| 2026-10-27 | 22700 | 26450 | 52300 | 61600 |
| 2026-11-03 | 22800 | 26550 | 52500 | 61800 |
| 2026-11-10 | 22850 | 26600 | 52700 | 62100 |
| 2026-11-17 | 22950 | 26700 | 52900 | 62400 |
| 2026-11-24 | 23000 | 26800 | 53100 | 62600 |
| 2026-12-01 | 23100 | 26900 | 53300 | 62900 |
| 2026-12-08 | 23200 | 27000 | 53500 | 63200 |
| 2026-12-15 | 23250 | 27100 | 53700 | 63500 |
| 2026-12-22 | 23350 | 27200 | 53900 | 63800 |
| 2026-12-29 | 23400 | 27300 | 54100 | 64100 |
| 2027-01-05 | 23500 | 27400 | 54300 | 64400 |
| 2027-01-12 | 23600 | 27500 | 54500 | 64700 |
| 2027-01-19 | 23650 | 27600 | 54700 | 65000 |
| 2027-01-26 | 23750 | 27700 | 54900 | 65300 |
| 2027-02-02 | 23850 | 27800 | 55100 | 65600 |
| 2027-02-09 | 23900 | 27900 | 55300 | 65900 |
| 2027-02-16 | 24000 | 28000 | 55500 | 66200 |
| 2027-02-23 | 24100 | 28100 | 55700 | 66500 |
| 2027-03-02 | 24150 | 28200 | 55900 | 66800 |
| 2027-03-09 | 24250 | 28300 | 56100 | 67100 |
| 2027-03-16 | 24350 | 28400 | 56300 | 67400 |
| 2027-03-23 | 24400 | 28500 | 56500 | 67700 |
| 2027-03-30 | 24500 | 28600 | 56700 | 68000 |
| 2027-04-06 | 24600 | 28700 | 56900 | 68300 |
| 2027-04-13 | 24700 | 28800 | 57100 | 68600 |
| 2027-04-20 | 24750 | 28900 | 57300 | 68900 |
| 2027-04-27 | 24850 | 29000 | 57500 | 69200 |
| 2027-05-04 | 24950 | 29100 | 57700 | 69500 |
| 2027-05-11 | 25050 | 29200 | 57900 | 69800 |
| 2027-05-18 | 25100 | 29300 | 58100 | 70100 |
| 2027-05-25 | 25200 | 29400 | 58300 | 70400 |
| 2027-06-01 | 25300 | 29500 | 58500 | 70700 |
| 2027-06-08 | 25400 | 29600 | 58700 | 71000 |
| 2027-06-15 | 25500 | 29700 | 58900 | 71300 |
| 2027-06-22 | 25600 | 29800 | 59100 | 71600 |
| 2027-06-29 | 25650 | 29900 | 59300 | 71900 |
| 2027-07-06 | 25750 | 30000 | 59500 | 72200 |
| 2027-07-13 | 25850 | 30100 | 59700 | 72500 |
| 2027-07-20 | 25950 | 30200 | 59900 | 72800 |
| 2027-07-27 | 26050 | 30300 | 60100 | 73100 |
| 2027-08-03 | 26150 | 30400 | 60300 | 73400 |
| 2027-08-10 | 26200 | 30500 | 60500 | 73700 |
| 2027-08-17 | 26300 | 30600 | 60700 | 74000 |
| 2027-08-24 | 26400 | 30700 | 60900 | 74300 |
| 2027-08-31 | 26500 | 30800 | 61100 | 74600 |
| 2027-09-07 | 26600 | 30900 | 61300 | 74900 |
| 2027-09-14 | 26700 | 31000 | 61500 | 75200 |
| 2027-09-21 | 26800 | 31100 | 61700 | 75500 |
| 2027-09-28 | 26900 | 31200 | 61900 | 75800 |
| 2027-10-05 | 27000 | 31300 | 62100 | 76100 |
| 2027-10-12 | 27050 | 31400 | 62300 | 76400 |
| 2027-10-19 | 27150 | 31500 | 62500 | 76700 |
| 2027-10-26 | 27200 | 31600 | 62700 | 77000 |
| 2027-11-02 | 27300 | 31700 | 62900 | 77300 |
| 2027-11-09 | 27350 | 31800 | 63100 | 77600 |
| 2027-11-16 | 27450 | 31900 | 63300 | 77900 |
| 2027-11-23 | 27500 | 32000 | 63500 | 78200 |
| 2027-11-30 | 27550 | 32100 | 63700 | 78500 |
| 2027-12-07 | 27650 | 32200 | 63900 | 78800 |
| 2027-12-14 | 27750 | 32300 | 64100 | 79100 |
| 2027-12-21 | 27800 | 32400 | 64300 | 79400 |
| 2027-12-28 | 27900 | 32500 | 64500 | 79700 |

## Notes

- NIFTY_1 / BANKNIFTY_1 are the planning levels for the **short put**; NIFTY_2 / BANKNIFTY_2 are the planning levels for the **short call**.
- These are planning levels, not live option-chain strikes. At entry, select the actual strikes by delta and IV; if the live 10–12Δ put or 15–18Δ call is materially different, use the live delta-derived strike.
- Long wings should normally sit around 5–8 delta and provide defined risk; wing width should be selected according to credit, liquidity, and portfolio risk rather than fixed distance alone.
- Terminal planning assumption for the broader thesis: NIFTY 30,000 and BANKNIFTY 71,000 by end-December 2027.
- Current reference levels used for the planning curve are approximately NIFTY 24,335 and BANKNIFTY 56,472; the curve is a smooth path to the terminal assumptions, not a market forecast.
- Tuesday is the expiry anchor for NIFTY weekly and BANKNIFTY monthly expiries; if Tuesday is a trading holiday, expiry moves to the previous trading day under NSE rules.
