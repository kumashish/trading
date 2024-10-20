# Predicting SPY weekly close levels
This is an attempt to predict weekly close values for next 52 weeks based on some time-series models. Since, this is a vwry rudimentary way, I won't advise anyone to use for live trading. One of the biggest drawbacks is that this exercise is only going tp use data of last 10 years, so this data doesn't even incorporate bigger crashes for last few years like that of 2000 and 2008 market down periods.
The data for thsi exercise is stored in ./data folder.
For SPY, file being used is SPY_HistoricalData_xxxxxxxxx.csv. This file contains historical data of daily close levels of spy for last 10 years.

Theory:
While no single formula guarantees accurate predictions, here are some of the best time-series forecasting models commonly used:

1. ARIMA (AutoRegressive Integrated Moving Average)
Use case: Best for predicting stock prices when data shows trends or seasonality.
Formula:
AR (AutoRegressive): 
𝑦
𝑡
=
𝜙
1
𝑦
𝑡
−
1
+
𝜙
2
𝑦
𝑡
−
2
+
⋯
+
𝜙
𝑝
𝑦
𝑡
−
𝑝
+
𝜖
𝑡
y 
t
​
 =ϕ 
1
​
 y 
t−1
​
 +ϕ 
2
​
 y 
t−2
​
 +⋯+ϕ 
p
​
 y 
t−p
​
 +ϵ 
t
​
 
MA (Moving Average): 
𝑦
𝑡
=
𝜖
𝑡
+
𝜃
1
𝜖
𝑡
−
1
+
𝜃
2
𝜖
𝑡
−
2
+
⋯
+
𝜃
𝑞
𝜖
𝑡
−
𝑞
y 
t
​
 =ϵ 
t
​
 +θ 
1
​
 ϵ 
t−1
​
 +θ 
2
​
 ϵ 
t−2
​
 +⋯+θ 
q
​
 ϵ 
t−q
​
 
Integrated (I) part controls differencing to handle non-stationarity.
Benefits:
Captures trends and lagged relationships well.
Often used for short- and mid-term forecasting.
Limitation: Doesn't handle large volatility changes well.
2. GARCH (Generalized Autoregressive Conditional Heteroskedasticity)
Use case: Best for modeling and forecasting financial time-series with varying volatility (e.g., stock prices, returns).
Formula:
𝜎
𝑡
2
=
𝛼
0
+
𝛼
1
𝜖
𝑡
−
1
2
+
𝛽
1
𝜎
𝑡
−
1
2
σ 
t
2
​
 =α 
0
​
 +α 
1
​
 ϵ 
t−1
2
​
 +β 
1
​
 σ 
t−1
2
​
 
Benefits:
Captures volatility clustering (periods of high/low volatility).
Important for risk management and derivatives pricing.
Limitation: Purely focuses on volatility, not the actual price level prediction.
3. LSTM (Long Short-Term Memory) - Neural Networks
Use case: Suitable for non-linear patterns, long-term dependencies, and capturing complex trends in stock prices.
Formula: LSTM doesn’t have a simple formula; it uses a series of gating mechanisms to capture long-term dependencies in data.
Benefits:
Great for sequential, complex, and non-linear relationships.
Can handle vast historical data and automatically discover patterns.
Limitation: Requires large data sets and considerable computational power.
4. Exponential Smoothing (ETS)
Use case: Best for smooth trends and seasonality in time series data (e.g., moving average levels, earnings forecasts).
Formula:
Simple: 
𝑆
𝑡
=
𝛼
𝑌
𝑡
+
(
1
−
𝛼
)
𝑆
𝑡
−
1
S 
t
​
 =αY 
t
​
 +(1−α)S 
t−1
​
 
Double: 
𝑆
𝑡
=
𝛼
𝑌
𝑡
+
(
1
−
𝛼
)
(
𝑆
𝑡
−
1
+
𝑇
𝑡
−
1
)
S 
t
​
 =αY 
t
​
 +(1−α)(S 
t−1
​
 +T 
t−1
​
 )
Benefits:
Works well with time series that show seasonality and trends.
Easy to implement.
Limitation: Not great for highly volatile data like stocks.
5. Prophet (by Facebook)
Use case: Useful for time-series data with clear seasonal effects and works well even with missing data.
Formula: It decomposes time-series data into trend, seasonality, and holidays/events. 
𝑦
(
𝑡
)
=
𝑔
(
𝑡
)
+
𝑠
(
𝑡
)
+
ℎ
(
𝑡
)
+
𝜖
𝑡
y(t)=g(t)+s(t)+h(t)+ϵ 
t
​
 , where:
𝑔
(
𝑡
)
g(t): Trend.
𝑠
(
𝑡
)
s(t): Seasonality.
ℎ
(
𝑡
)
h(t): Holiday or special events.
Benefits:
Easy to use and interpret.
Flexible with irregular data points (e.g., missing data).
Limitation: Not designed for high-frequency data like stock ticks.
6. Kalman Filter
Use case: Suitable for noisy data and filtering out short-term fluctuations to predict more stable stock price trends.
Formula: It's based on state-space models, which consist of a state equation and a measurement equation.
State equation: 
𝑥
𝑡
=
𝐴
𝑥
𝑡
−
1
+
𝐵
𝑢
𝑡
+
𝑤
𝑡
x 
t
​
 =Ax 
t−1
​
 +Bu 
t
​
 +w 
t
​
 
Measurement equation: 
𝑦
𝑡
=
𝐶
𝑥
𝑡
+
𝑣
𝑡
y 
t
​
 =Cx 
t
​
 +v 
t
​
 
Benefits:
Captures latent variables and dynamic systems.
Good for filtering and smoothing data in noisy environments.
Limitation: More complex to implement and understand.
Choosing the Best Model:
ARIMA/ARIMAX: For price-level predictions in shorter terms with trends or seasonality.
GARCH: For volatility predictions (risk management).
LSTM: For non-linear and complex patterns in long-term data.
ETS/Prophet: For simpler forecasts when the data shows seasonality.
Kalman Filter: For noise reduction and trend filtering.

Steps:
1. Extract the weekly close from the actual data.
