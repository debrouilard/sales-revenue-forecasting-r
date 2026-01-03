from src.data_loader import load_sales_data
from src.visualization import plot_sales, plot_forecast
from src.forecasting import forecast_arima, forecast_ets

def main():
    # Load data
    df = load_sales_data('data/stores_sales_forecasting.csv')
    
    # Plot historical sales
    plot_sales(df)
    
    # ARIMA Forecast
    arima_forecast = forecast_arima(df)
    plot_forecast(df, arima_forecast, title='ARIMA Forecast')
    
    # ETS Forecast
    ets_forecast = forecast_ets(df)
    plot_forecast(df, ets_forecast, title='ETS Forecast')

if __name__ == "__main__":
    main()
