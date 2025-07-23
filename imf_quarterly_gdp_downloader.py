# imf_annual_gdp_downloader.py

from pandasdmx import Request
import pandas as pd
import os
import time

INDICATOR_CODE = "NGDP_R_XDC"
START_YEAR = "2010"
END_YEAR = "2024"

COUNTRIES = {
    "United States": "US",
    "China": "CN",
    "Germany": "DE",
    "India": "IN",
    "Japan": "JP",
    "United Kingdom": "GB",
    "France": "FR",
    "Italy": "IT",
    "Canada": "CA",
    "Brazil": "BR",
    "Russia": "RU",
    "Spain": "ES",
    "South Korea": "KR",
    "Australia": "AU",
    "Mexico": "MX",
    "Turkey": "TR",
    "Indonesia": "ID",
    "Netherlands": "NL",
    "Saudi Arabia": "SA",
    "Poland": "PL",
    "Switzerland": "CH",
    "Taiwan": "TW",
    "Belgium": "BE",
    "Argentina": "AR",
    "Sweden": "SE",
    "Ireland": "IE",
    "Israel": "IL",
    "Singapore": "SG",
    "United Arab Emirates": "AE",
    "Thailand": "TH",
    "Austria": "AT",
    "Norway": "NO",
    "Philippines": "PH",
    "Vietnam": "VN",
    "Bangladesh": "BD",
    "Denmark": "DK",
    "Malaysia": "MY",
    "Colombia": "CO",
    "Hong Kong": "HK",
    "South Africa": "ZA",
    "Romania": "RO",
    "Pakistan": "PK",
    "Czech Republic": "CZ",
    "Egypt": "EG",
    "Chile": "CL",
    "Iran": "IR",
    "Portugal": "PT",
    "Finland": "FI",
    "Peru": "PE",
    "Kazakhstan": "KZ",
    "Algeria": "DZ",
    "Greece": "GR",
}

def fetch_and_save(country_name, country_code):
    try:
        req = Request("IMF")
        resp = req.data(
            resource_id="IFS",
            key=f"{country_code}.A.{INDICATOR_CODE}",
            params={"startPeriod": START_YEAR, "endPeriod": END_YEAR}
        )
        series = next(resp.data.series.values())
        data = pd.DataFrame(series.obs(), columns=["Year", "GDP"])
        if data.empty:
            print(f"⚠️ No data for {country_name}")
            return

        os.makedirs("data", exist_ok=True)
        filename = f"data/{country_code.lower()}_annual_real_gdp.csv"
        data.to_csv(filename, index=False)
        print(f"✅ {country_name} → {filename}")
    except Exception as e:
        print(f"❌ {country_name} ({country_code}) failed: {e}")

def main():
    for name, code in COUNTRIES.items():
        fetch_and_save(name, code)
        time.sleep(1)

if __name__ == "__main__":
    main()
