import pandas as pd

def load_sales_data(filepath: str, freq='M') -> pd.DataFrame:
    """
    Load sales CSV with 'Date' and 'Revenue' columns.
    """
    df = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    df = df.asfreq(freq)
    return df
