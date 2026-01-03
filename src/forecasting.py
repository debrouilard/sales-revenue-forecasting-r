from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pmdarima import auto_arima
import pandas as pd

def forecast_arima(df: pd.DataFrame, periods=12) -> pd.DataFrame:
    model = auto_arima(df['Revenue'], seasonal=True, m=12, trace=False)
    arima_model = ARIMA(df['Revenue'], order=model.order, seasonal_order=model.seasonal_order)
    arima_result = arima_model.fit()
    
    forecast = arima_result.get_forecast(steps=periods)
    forecast_index = pd.date_range(start=df.index[-1] + pd.offsets.MonthBegin(1), periods=periods, freq='M')
    forecast_df = pd.DataFrame({'Forecast': forecast.predicted_mean}, index=forecast_index)
    return forecast_df

def forecast_ets(df: pd.DataFrame, periods=12) -> pd.Series:
    ets_model = ExponentialSmoothing(df['Revenue'], seasonal='add', seasonal_periods=12).fit()
    forecast = ets_model.forecast(periods)
    return forecast
