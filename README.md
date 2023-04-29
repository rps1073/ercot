# Overview

The main script `task.py` loops through all of the source data and outputs the months where the average monthly price of power was above $100/MWh.

`get_monthly_qualifying_averages.py` is a utility function that returns the year/month combinations where average settlement point > $100/MWh

`/data` contains the raw Excel files from the ERCOT website. Note: the zip file containing this code only has `rpt.00013061.0000000000000000.RTMLZHBSPP_2021.xlsx` to save on space, but the code initially ran against all Excel files from the ERCOT website containing historical data from 2010-2022.

# How to run the script

Run `python3 task.py` to start the primary script that reads the data and outputs the qualifying monthly averages

# Assumptions
- The source data from the ERCOT website has already been downloaded from their website and the underlying Excel files are available in some form of local storage (ex. `/data` folder) for easier access

