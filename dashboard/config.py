import pandas as pd
import streamlit as st
import os

# Application configuration
APP_TITLE = "HHS UAC Capacity Analytics"
APP_ICON = "📊"

# Path to data
DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/processed/uac_metrics.csv'))

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# KPI Color Coding Logic
def kpi_color(value, threshold_yellow, threshold_red, direction="lower_is_better"):
    if direction == "lower_is_better":
        if value < threshold_yellow:
            return "normal" # Streamlit doesn't support custom colors in metric natively, so we use normal/inverse
        elif value < threshold_red:
            return "off"
        else:
            return "inverse"
    else:
        if value > threshold_yellow:
            return "normal"
        elif value > threshold_red:
            return "off"
        else:
            return "inverse"
