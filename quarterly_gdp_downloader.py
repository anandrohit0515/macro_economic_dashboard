# quarterly_gdp_downloader.py

import os
import pandas as pd
from fredapi import Fred

# Replace this with your FRED API key
FRED_API_KEY = "d83494fbb042655f9b8a652fd8da0004"

fred = Fred(api_key=FRED_API_KEY)

# FRED GDP series IDs (quarterly, seasonally adjusted annual rates)
series_map = {
    'USA': ('GDP', 'usa_quarterly_gdp.csv'),         # US GDP
    'CAN': ('NGDPRSAXDCACQ', 'can_quarterly_gdp.csv'),  # Canada GDP
}

def fetch_quarterly_gdp(series_id, filename):
    try:
        data = fred.get_series(series_id)
        df = data.reset_index()
        df.columns = ['Date', 'GDP']
        df = df[df['Date'] >= '2015-01-01']
        os.makedirs("data", exist_ok=True)
        df.to_csv(f"data/{filename}", index=False)
        print(f"✅ Saved: {filename}")
    except Exception as e:
        print(f"❌ Error fetching {series_id}: {e}")

def main():
    for code, (series_id, filename) in series_map.items():
        fetch_quarterly_gdp(series_id, filename)

if __name__ == "__main__":
    main()
