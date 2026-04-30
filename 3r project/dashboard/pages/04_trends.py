import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from config import load_data

st.set_page_config(page_title="Comparative & Trend Analysis", page_icon="📈", layout="wide")
st.title("Comparative & Trend Analysis")

df = load_data()
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

st.markdown("### Year-over-Year Monthly Comparison")
metric_options = ['Total System Load', 'Children apprehended and placed in CBP custody', 'Children discharged from HHS Care']
selected_metric = st.selectbox("Select Metric", metric_options)

yoy_data = df.groupby(['Year', 'Month'])[selected_metric].mean().reset_index()

fig = px.bar(yoy_data, x='Month', y=selected_metric, color='Year', barmode='group',
             title=f'YoY Monthly Average: {selected_metric}',
             labels={'Month': 'Month of Year'})
fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.plotly_chart(fig, use_container_width=True)

st.markdown("### Cumulative Discharges vs Cumulative Intake")
df['Cumulative Intake'] = df['Children apprehended and placed in CBP custody'].cumsum()
df['Cumulative Discharges'] = df['Children discharged from HHS Care'].cumsum()

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df['Date'], y=df['Cumulative Intake'], name='Cumulative Intake', line=dict(color='blue')))
fig2.add_trace(go.Scatter(x=df['Date'], y=df['Cumulative Discharges'], name='Cumulative Discharges', line=dict(color='green')))
fig2.update_layout(title='Cumulative Discharges vs Intake')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### Distribution Comparison (Box Plots)")
fig3 = px.box(df, x='Year', y=selected_metric, title=f'Distribution of {selected_metric} by Year')
st.plotly_chart(fig3, use_container_width=True)
