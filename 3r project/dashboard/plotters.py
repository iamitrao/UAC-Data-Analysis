import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Standard colors
COLOR_CBP = '#1f77b4' # Blue
COLOR_HHS = '#2ca02c' # Green
COLOR_RED = '#d62728'

def plot_system_load(df, start_date, end_date):
    filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Children in CBP custody'], 
                             mode='lines', name='CBP Custody', line=dict(color=COLOR_CBP)))
    fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['Children in HHS Care'], 
                             mode='lines', name='HHS Care', line=dict(color=COLOR_HHS)))
    
    # Shade high load periods (e.g. Total System Load > 75th percentile)
    threshold = df['Total System Load'].quantile(0.75)
    high_load = filtered_df[filtered_df['Total System Load'] > threshold]
    
    # We could add vrects for high load, but keeping it simple for now
    
    fig.update_layout(title='System Load Time-Series', xaxis_title='Date', yaxis_title='Number of Children', hovermode='x unified')
    return fig

def plot_daily_flows(df, start_date, end_date):
    filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=filtered_df['Date'], y=filtered_df['Children apprehended and placed in CBP custody'],
                         name='Apprehensions', marker_color=COLOR_CBP))
    fig.add_trace(go.Bar(x=filtered_df['Date'], y=filtered_df['Children discharged from HHS Care'],
                         name='Discharges', marker_color=COLOR_HHS))
    fig.update_layout(title='Daily Apprehensions & Discharges', barmode='group')
    return fig

def plot_net_intake(df, start_date, end_date, window=7):
    filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    
    col_name = 'Net Daily Intake'
    if window == 7:
        col_name = 'Net Daily Intake (7-day avg)'
    else:
        filtered_df[f'Net Daily Intake ({window}-day avg)'] = filtered_df['Net Daily Intake'].rolling(window=window, min_periods=1).mean()
        col_name = f'Net Daily Intake ({window}-day avg)'
        
    fig = px.line(filtered_df, x='Date', y=col_name, title=f'{window}-Day Rolling Avg Net Intake')
    fig.add_hline(y=0, line_dash="dash", line_color="black")
    return fig

def plot_backlog_accumulation(df, start_date, end_date):
    filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    fig = px.area(filtered_df, x='Date', y='Backlog Pressure Index', title='Backlog Accumulation Trend')
    return fig

def plot_waterfall(df):
    fig = go.Figure(go.Waterfall(
        name='Pipeline', orientation='v',
        measure=['relative', 'relative', 'relative', 'total'],
        x=['Apprehensions', 'Transfers In', 'Discharges', 'Net Growth'],
        y=[df['Children apprehended and placed in CBP custody'].sum(), 
           df['Children transferred out of CBP custody'].sum(), 
           -df['Children discharged from HHS Care'].sum(), 
           0],
        connector={"line":{"color":"rgb(63, 63, 63)"}}
    ))
    fig.update_layout(title='Cumulative Pipeline Flow Waterfall')
    return fig

def plot_efficiency_ratio(df, start_date, end_date):
    filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    fig = px.line(filtered_df, x='Date', y=['CBP Efficiency Ratio', 'Discharge Capacity Ratio'], 
                  title='Pipeline Efficiency Ratios (%)')
    fig.add_hline(y=50, line_dash='dash', line_color='red', annotation_text='50% Benchmark')
    return fig
