Predicting SPY Weekly Close Levels
==================================
## Theory
Here are some commonly used time-series forecasting models:

---

### 1. ARIMA (AutoRegressive Integrated Moving Average)

- **Use case:** Predicting stock prices with trends or seasonality.
- **Formula:**
  - **AR (AutoRegressive):**  
    `y_t = ϕ₁y_{t-1} + ϕ₂y_{t-2} + ... + ϕ_py_{t-p} + ϵ_t`
  - **MA (Moving Average):**  
    `y_t = ϵ_t + θ₁ϵ_{t-1} + θ₂ϵ_{t-2} + ... + θ_qϵ_{t-q}`
  - Integrated (I) part controls differencing for non-stationary data.
- **Benefits:**  
  Captures trends and lagged relationships, suitable for short- and mid-term forecasting.
- **Limitation:**  
  Does not handle large volatility changes well.

---

### 2. GARCH (Generalized Autoregressive Conditional Heteroskedasticity)

- **Use case:** Modeling & forecasting financial series with changing volatility.
- **Formula:**  
  `σ²_t = α₀ + α₁ϵ²_{t-1} + β₁σ²_{t-1}`
- **Benefits:**  
  Captures volatility clustering (periods of high/low volatility); important for risk management.
- **Limitation:**  
  Focuses on volatility, not actual price level prediction.

---

### 3. LSTM (Long Short-Term Memory Neural Networks)

- **Use case:** Non-linear patterns, long-term dependencies, complex trends.
- **Formula:**  
  No simple formula; uses gating mechanisms to capture dependencies.
- **Benefits:**  
  Handles sequential, complex, and non-linear relationships; can utilize vast data.
- **Limitation:**  
  Requires large datasets and significant computational power.

---

### 4. Exponential Smoothing (ETS)

- **Use case:** Smooth trends/seasonality in time series (e.g., moving averages, earnings).
- **Formula:**
  - **Simple:**  
    `S_t = αY_t + (1−α)S_{t-1}`
  - **Double:**  
    `S_t = αY_t + (1−α)(S_{t-1} + T_{t-1})`
- **Benefits:**  
  Works well with seasonality and trends, easy to implement.
- **Limitation:**  
  Not ideal for highly volatile data like stocks.

---

### 5. Prophet (by Facebook)

- **Use case:** Time-series with clear seasonal effects, works with missing data.
- **Formula:**  
  `y(t) = g(t) + s(t) + h(t) + ϵ_t`  
  where:
    - `g(t)` = trend,
    - `s(t)` = seasonality,
    - `h(t)` = holidays/events.
- **Benefits:**  
  Easy to use and interpret, flexible with irregular data points.
- **Limitation:**  
  Not designed for high-frequency data like stock ticks.

---

### 6. Kalman Filter

- **Use case:** Noisy data, filtering out short-term fluctuations for stable trend prediction.
- **Formula:**
  - **State equation:**  
    `x_t = A x_{t-1} + B u_t + w_t`
  - **Measurement equation:**  
    `y_t = C x_t + v_t`
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
