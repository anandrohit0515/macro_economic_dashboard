import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit config
st.set_page_config(page_title="WEO GDP Dashboard", layout="wide")
st.title("🌍 World GDP Dashboard (1980–2030)")

# Load the data
df = pd.read_csv("/Users/gaurikanand/macro_economic_dashboard/data/WEO_Filter.csv")

# Convert year columns to numeric (if needed)
year_columns = [col for col in df.columns if col.isdigit()]
df[year_columns] = df[year_columns].apply(pd.to_numeric, errors='coerce')

# Sidebar: Indicator & Year selection
indicators = df['INDICATOR'].unique().tolist()
selected_indicator = st.sidebar.selectbox("Select Indicator", indicators)

available_years = sorted([int(col) for col in year_columns])
selected_year = st.sidebar.selectbox("Select Year", available_years)

# Filter data
filtered_df = df[df['INDICATOR'] == selected_indicator]
filtered_df = filtered_df[['COUNTRY', 'SCALE', str(selected_year)]].dropna()
filtered_df = filtered_df.sort_values(by=str(selected_year), ascending=False)

# Bar Chart
st.subheader(f"{selected_indicator} — {selected_year}")
fig = px.bar(
    filtered_df,
    x='COUNTRY',
    y=str(selected_year),
    text=str(selected_year),
    labels={str(selected_year): 'Value', 'COUNTRY': 'Country'},
    color=str(selected_year),
    color_continuous_scale='Blues',
)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# Data Table
with st.expander("📄 Show Raw Data"):
    st.dataframe(filtered_df.reset_index(drop=True))
