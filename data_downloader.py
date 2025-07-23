# data_downloader.py

import os
import pandas as pd
import requests

def fetch_gdp_data(country_code, filename):
    indicator_code = 'NY.GDP.MKTP.CD'
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=100"
    response = requests.get(url)
    try:
        raw = response.json()
        if len(raw) < 2 or not isinstance(raw[1], list):
            print(f"⚠️ No data for {country_code}")
            return

        df = pd.DataFrame(raw[1])
        df = df[['date', 'value']].dropna()
        df.columns = ['Year', 'GDP']
        df['Year'] = df['Year'].astype(int)
        df = df.sort_values('Year')

        os.makedirs("data", exist_ok=True)
        df.to_csv(f"data/{filename}", index=False)
        print(f"✅ Saved {filename}")
    except Exception as e:
        print(f"❌ Failed to fetch data for {country_code}: {e}")

def main():
    countries = {
        'USA': 'usa_gdp.csv',
        'CAN': 'can_gdp.csv',
        'IND': 'ind_gdp.csv',
        'CHN': 'chn_gdp.csv',
    }
    for code, file in countries.items():
        fetch_gdp_data(code, file)

if __name__ == "__main__":
    main()
