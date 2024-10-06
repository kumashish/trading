# Predicting SPY weekly close levels
This is an attempt to predict weekly close values for next 52 weeks based on some time-series models. Since, this is a vwry rudimentary way, I won't advise anyone to use for live trading. One of the biggest drawbacks is that this exercise is only going tp use data of last 10 years, so this data doesn't even incorporate bigger crashes for last few years like that of 2000 and 2008 market down periods.
The data for thsi exercise is stored in ./data folder.
For SPY, file being used is SPY_HistoricalData_xxxxxxxxx.csv. This file contains historical data of daily close levels of spy for last 10 years.
Steps:
1. Extract the weekly close from the actual data.
