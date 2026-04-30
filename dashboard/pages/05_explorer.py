import streamlit as st
import sys
import os
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import load_data

st.set_page_config(page_title="Data Explorer & Export", page_icon="🗄️", layout="wide")
st.title("Data Explorer & Export")

df = load_data()

st.sidebar.header("Filter Data")
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

selected_columns = st.sidebar.multiselect("Select Columns", df.columns, default=['Date', 'Total System Load', 'Net Daily Intake', 'Children in CBP custody', 'Children in HHS Care'])

filtered_df = df[(df['Date'].dt.date >= start_date) & (df['Date'].dt.date <= end_date)][selected_columns]

# Interactive Data Table using AgGrid
gb = GridOptionsBuilder.from_dataframe(filtered_df)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children")
gridOptions = gb.build()

st.markdown("### Interactive Data Table")
AgGrid(
    filtered_df,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT', 
    update_mode='MODEL_CHANGED', 
    fit_columns_on_grid_load=False,
    theme='streamlit',
    enable_enterprise_modules=True,
    height=500, 
    width='100%',
    reload_data=True
)

st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='uac_data_export.csv',
    mime='text/csv',
)
