import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import load_data
from plotters import plot_net_intake, plot_backlog_accumulation

st.set_page_config(page_title="Capacity Pressure & Risk Analysis", page_icon="⚠️", layout="wide")
st.title("Capacity Pressure & Risk Analysis")

df = load_data()

min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
with col2:
    end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

window = st.radio("Rolling Average Window", [7, 14], horizontal=True)

st.plotly_chart(plot_net_intake(df, start_date, end_date, window), use_container_width=True)

st.plotly_chart(plot_backlog_accumulation(df, start_date, end_date), use_container_width=True)

# Heatmap: Monthly Net Intake
st.markdown("### Monthly Net Intake Heatmap")
df['Year'] = df['Date'].dt.year
df['Month_Name'] = df['Date'].dt.month_name()
df_filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
heatmap_data = df_filtered.pivot_table(values='Net Daily Intake', index='Month_Name', columns='Year', aggfunc='sum')
# Reorder months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
heatmap_data = heatmap_data.reindex(months)

fig = px.imshow(heatmap_data, color_continuous_scale='RdYlGn_r', aspect="auto")
st.plotly_chart(fig, use_container_width=True)

# Volatility Index
st.markdown("### Volatility Index (14-day rolling std dev of system load)")
df_filtered['Volatility Index'] = df_filtered['Total System Load'].rolling(window=14, min_periods=1).std()
fig2 = px.line(df_filtered, x='Date', y='Volatility Index', title='Volatility Index')
st.plotly_chart(fig2, use_container_width=True)
