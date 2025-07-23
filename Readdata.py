import pandas as pd

# Load the CSV
df = pd.read_csv("/Users/gaurikanand/macro_economic_dashboard/data/WEO.csv")

# View the structure
#print(df.columns)
#print(df.head())
#import pandas as pd

# Load the CSV file
#df = pd.read_csv("WEO.csv")

# Define the list of countries
countries = [
    "United States", "China", "Germany", "India", "Japan", "United Kingdom",
    "France", "Italy", "Canada", "Brazil", "Russia", "Spain", "South Korea",
    "Australia", "Mexico", "Turkey", "Indonesia", "Netherlands", "Saudi Arabia",
    "Poland", "Switzerland", "Taiwan", "Belgium", "Argentina", "Sweden",
    "Ireland", "Israel", "Singapore", "United Arab Emirates", "Thailand",
    "Austria", "Norway", "Philippines", "Vietnam", "Bangladesh", "Denmark",
    "Malaysia", "Colombia", "Hong Kong", "South Africa", "Romania", "Pakistan",
    "Czech Republic", "Egypt", "Chile", "Iran", "Portugal", "Finland", "Peru",
    "Kazakhstan", "Algeria", "Greece"
]

# Define the indicators to keep
indicators = [
    "Gross domestic product (GDP), Current prices, US dollar",
    "Gross domestic product (GDP), Current prices, Per capita, US dollar"
]

# Filter the DataFrame
filtered_df = df[
    (df['COUNTRY'].isin(countries)) &
    (df['INDICATOR'].isin(indicators))
]

# Select only the required columns
result = filtered_df[['COUNTRY', 'INDICATOR', 'SCALE', '1980','1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', 
                      '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', 
                      '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                        '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', 
                        '2021', '2022' ,'2023','2024', '2025', '2026', '2027', '2028', '2029', '2030']]

# Display the filtered result
print(result)

# Save the filtered DataFrame to a new CSV file
output_path = "/Users/gaurikanand/macro_economic_dashboard/data/WEO_Filter.csv"
result.to_csv(output_path, index=False)
print("✅ Filtered data saved to 'filtered_gdp_1980.csv'")

