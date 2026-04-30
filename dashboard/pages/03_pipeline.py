import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import load_data
from plotters import plot_waterfall, plot_efficiency_ratio

st.set_page_config(page_title="Pipeline Flow & Efficiency", page_icon="🚰", layout="wide")
st.title("Pipeline Flow & Efficiency")

df = load_data()

min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
with col2:
    end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

df_filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

st.plotly_chart(plot_waterfall(df_filtered), use_container_width=True)

st.plotly_chart(plot_efficiency_ratio(df, start_date, end_date), use_container_width=True)

st.markdown("### Lag Analysis (Intake to Transfer)")
# Shift transfers by 1, 2, 3 days and calculate correlation
lag_options = [1, 2, 3]
lag = st.selectbox("Select Lag (Days)", lag_options)

df_filtered['Lagged Transfers'] = df_filtered['Children transferred out of CBP custody'].shift(-lag)

fig = px.scatter(df_filtered, x='Children apprehended and placed in CBP custody', y='Lagged Transfers',
                 title=f'Apprehensions vs Transfers ({lag} Days Later)', trendline='ols')
st.plotly_chart(fig, use_container_width=True)
