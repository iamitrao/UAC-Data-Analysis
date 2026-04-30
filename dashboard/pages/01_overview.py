import streamlit as st
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import load_data
from plotters import plot_system_load, plot_daily_flows
import datetime

st.set_page_config(page_title="System Overview", page_icon="📊", layout="wide")
st.title("System Overview")

df = load_data()

# Global Controls
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
with col2:
    end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

# KPI Summary Cards
latest_data = df[df['Date'] <= pd.to_datetime(end_date)].iloc[-1]
avg_system_load = df['Total System Load'].mean()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Children Under Care", int(latest_data['Total System Load']), 
            delta=f"{int(latest_data['Total System Load'] - avg_system_load)} vs avg", delta_color="inverse")
kpi2.metric("Net Intake Pressure (7-day avg)", f"{latest_data['Net Daily Intake (7-day avg)']:.1f}")
kpi3.metric("Discharge Capacity Ratio", f"{latest_data['Discharge Capacity Ratio']:.1f}%")
kpi4.metric("CBP Efficiency Ratio", f"{latest_data['CBP Efficiency Ratio']:.1f}%")

st.markdown("---")

st.plotly_chart(plot_system_load(df, start_date, end_date), use_container_width=True)

st.plotly_chart(plot_daily_flows(df, start_date, end_date), use_container_width=True)
