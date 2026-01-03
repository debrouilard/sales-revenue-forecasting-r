import pandas as pd

def load_sales_data(filepath: str) -> pd.DataFrame:
    """
    Load a Kaggle sales CSV and return monthly aggregated sales.
    """
    # Read CSV with proper encoding
    df = pd.read_csv(filepath, parse_dates=['Order Date'], encoding='latin1')
    
    # Keep only the necessary columns and rename Sales -> Revenue
    df = df[['Order Date', 'Sales']].rename(columns={'Sales': 'Revenue'})
    
    # Set date as index
    df = df.set_index('Order Date')
    
    # Aggregate monthly
    df = df.resample('M').sum()
    
    return df
