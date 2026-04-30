import streamlit as st

st.set_page_config(
    page_title="HHS Capacity Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("HHS UAC Capacity Analysis Dashboard")

st.markdown("""
Welcome to my data analysis dashboard for the Unaccompanied Alien Children (UAC) Program!

I built this app to visualize the flow of children through the CBP and HHS systems. Use the sidebar on the left to check out the different analysis pages I made:

- **01 Overview**: A quick look at the total numbers and daily flow.
- **02 Pressure**: Graphs showing when the system gets backed up and stressed.
- **03 Pipeline**: Looking at how efficiently kids are transferred and discharged.
- **04 Trends**: Comparing data across different months and years.
- **05 Explorer**: A raw data table where you can filter and download the metrics I calculated.
""")

st.sidebar.info("Select a page above to get started.")
