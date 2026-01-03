import matplotlib.pyplot as plt
import pandas as pd

def plot_sales(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Revenue'], marker='o')
    plt.title('Sales Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.grid(True)
    plt.show()

def plot_forecast(df: pd.DataFrame, forecast: pd.DataFrame, title='Forecast'):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Revenue'], label='Actual')
    plt.plot(forecast, label='Forecast', marker='o')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.legend()
    plt.grid(True)
    plt.show()
