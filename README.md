Predicting SPY Weekly Close Levels
==================================

This repository attempts to predict SPY (S&P 500 ETF) weekly close values for the next 52 weeks using several time-series models. This is a very rudimentary approach and **not** recommended for live trading.

**Data:**  
- Data is stored in the `./data` folder.
- For SPY, the file used is `SPY_HistoricalData_xxxxxxxxx.csv`, which contains the daily close levels for the past 10 years.

---

## Theory

While no single formula guarantees accurate predictions, here are some commonly used time-series forecasting models:

---

### 1. ARIMA (AutoRegressive Integrated Moving Average)

- **Use case:** Predicting stock prices with trends or seasonality.
- **Benefits:**  
  Captures trends and lagged relationships, suitable for short- and mid-term forecasting.
- **Limitation:**  
  Does not handle large volatility changes well.
---

### 2. GARCH (Generalized Autoregressive Conditional Heteroskedasticity)

- **Use case:** Modeling & forecasting financial series with changing volatility.
- **Benefits:**  
  Captures volatility clustering (periods of high/low volatility); important for risk management.
- **Limitation:**  
  Focuses on volatility, not actual price level prediction.
---

### 3. LSTM (Long Short-Term Memory Neural Networks)

- **Use case:** Non-linear patterns, long-term dependencies, complex trends.
- **Benefits:**  
  Handles sequential, complex, and non-linear relationships; can utilize vast data.
- **Limitation:**  
  Requires large datasets and significant computational power.

---

### 4. Exponential Smoothing (ETS)

- **Use case:** Smooth trends/seasonality in time series (e.g., moving averages, earnings).
- **Benefits:**  
  Works well with seasonality and trends, easy to implement.
- **Limitation:**  
  Not ideal for highly volatile data like stocks.

---

### 5. Prophet (by Facebook)

- **Use case:** Time-series with clear seasonal effects, works with missing data.
- **Benefits:**  
  Easy to use and interpret, flexible with irregular data points.
- **Limitation:**  
  Not designed for high-frequency data like stock ticks.

---

### 6. Kalman Filter

- **Use case:** Noisy data, filtering out short-term fluctuations for stable trend prediction.
- **Benefits:**  
  Captures latent variables and dynamic systems, good for filtering and smoothing.
- **Limitation:**  
  More complex to implement and understand.

---

## Choosing the Best Model

- **ARIMA/ARIMAX:** Short-term price-level predictions with trend/seasonality.
- **GARCH:** Volatility prediction (risk management).
- **LSTM:** Non-linear, complex patterns in long-term data.
- **ETS/Prophet:** Simpler forecasts with seasonality.
- **Kalman Filter:** Noise reduction and trend filtering.

---

## Steps

1. Extract the weekly close from the actual data.

---
