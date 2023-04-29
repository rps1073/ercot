import pandas as pd
from os import listdir
from utilities.get_monthly_qualifying_averages import get_monthly_qualifying_averages

print("Starting task")

files = listdir("data")

for file in files:
    try:
        workbook = pd.ExcelFile(f"./data/{file}")

        print(f"Grabbing data for {file}")
        result = get_monthly_qualifying_averages(workbook)
        if not result.empty:
            print(result)
    except Exception as e:
        print(e)

print("Task complete")
