# Deployed Link
https://huggingface.co/spaces/iamitrao/UAC-Capacity-Dashboard




# HHS UAC Data Analysis Project

This is my data analysis project analyzing the Unaccompanied Alien Children (UAC) Program data from HHS. The goal of this project is to figure out when the system gets overwhelmed and see where the bottlenecks are in the process from CBP custody to HHS care and final discharge.

## What's in this project?
- `data/`: The raw CSV dataset and the processed metrics file I made.
- `notebooks/`: Jupyter notebooks where I did data cleaning, calculated metrics, and plotted graphs.
- `dashboard/`: A Streamlit dashboard I built to visualize the data interactively.
- `reports/`: My final project report summarizing my findings.

## How to run it

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the data processing notebook:
   Open `notebooks/1_Data_Cleaning_and_Metrics.ipynb` and run all cells. This creates the clean data file in the `data/processed/` folder.

3. Start the dashboard:
   ```bash
   streamlit run dashboard/app.py
   ```

If you have any questions about the analysis, check out the `reports` folder!
