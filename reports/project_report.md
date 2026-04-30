# Data Analysis Project: Unaccompanied Alien Children (UAC) Care Capacity

**Project Overview**
For this project, I analyzed data from the Department of Health and Human Services (HHS) regarding the Unaccompanied Alien Children (UAC) program. My main goal was to figure out when the system gets overwhelmed and where the biggest bottlenecks are happening between Customs and Border Protection (CBP) and HHS care.

## 1. Data Cleaning
The raw data came in a CSV file that needed some work. In my Jupyter notebook (`notebooks/1_Data_Cleaning_and_Metrics.ipynb`), I did the following:
- Clean up the column names because some had weird asterisks in them.
- Convert the dates from strings like "December 21, 2025" into actual datetime objects.
- Remove commas from the numbers (like "2,484") so I could convert them into integers.
- Fill in missing dates. There were some gaps in the data, so I used a forward-fill method for the active custody numbers and filled the daily apprehension/discharge numbers with zeros.

## 2. Key Metrics I Created
To actually understand the pressure on the system, the raw numbers weren't enough. In the same notebook, I calculated a few new metrics:
- **Total System Load**: Just adding the kids in CBP custody and HHS care together.
- **Net Daily Intake**: The number of kids transferred into HHS minus the number discharged. If this is positive for too long, a backlog builds up.
- **Discharge Capacity Ratio**: The percentage of kids in HHS care who get discharged each day. This helps show how fast HHS is finding sponsors.

## 3. What I Found (Exploratory Data Analysis)

I made a Streamlit dashboard (`dashboard/app.py`) to show my findings interactively, but here are the main takeaways:

**1. Seasonal Spikes overwhelm CBP early on:**
There are clear times of the year (mostly spring/summer) when apprehensions spike. During these times, CBP gets overwhelmed very quickly.

**2. The biggest bottleneck is discharging kids, not transferring them:**
When I looked at the pipeline, CBP is actually pretty good at transferring kids to HHS. The problem is that HHS can't discharge them to vetted sponsors fast enough. The discharge rate is pretty flat, so when a huge wave of kids comes in, they get stuck in HHS care, building up a massive backlog.

**3. The 2-3 Day Lag:**
By shifting the data a few days and running a scatter plot, I found a lag. A big spike in border apprehensions usually hits the HHS system about 2 to 3 days later. This is super important because it gives HHS a 2-day warning to get beds ready before the kids actually arrive.

## 4. Suggestions based on the data
Based on my analysis, I think the system could be improved by:
- **Using the 2-day warning:** Since we know there's a lag, HHS should use the daily apprehension numbers to immediately start preparing staff, rather than waiting for the kids to actually be transferred.
- **Focusing on the discharge process:** The data shows that getting kids out of HHS care is the slowest part of the whole pipeline. Putting more resources into vetting sponsors faster would clear up the backlog way better than just building more beds.
