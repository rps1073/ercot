import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'


def get_monthly_qualifying_averages(file):
    """
    Args:
        file: the name of the Excel file that will be read into the function

    Returns:
        The average monthly settlement point price and associated year/month where average_monthly_settlement_price > $100/MWh
    """
    ercot = pd.concat(pd.read_excel(file, sheet_name=None), ignore_index=True)
    hb_west_settlements = ercot[ercot["Settlement Point Name"] == "HB_WEST"]

    hb_west_settlements["Delivery Month"] = pd.to_datetime(
        hb_west_settlements["Delivery Date"]
    ).dt.month
    hb_west_settlements["Delivery Year"] = pd.to_datetime(
        hb_west_settlements["Delivery Date"]
    ).dt.year

    averages = (
        hb_west_settlements.groupby(["Delivery Year", "Delivery Month"])[
            "Settlement Point Price"
        ]
        .mean()
        .reset_index(name="Average Monthly Settlement Price")
    )
    qualifying_averages = averages[averages["Average Monthly Settlement Price"] > 100]

    return qualifying_averages
