#!python3

# progress.py - This subroutine is to calculate how I am progressing this will
#               read in data and crunch metrics on how I am doing
#


import pandas as pd


def progressWeekly(date):
    # read in the csv containing all my body data
    df_bodyStats = pd.read_csv("databases/bodyStats.csv", encoding="utf-8")

    print(df_bodyStats.head())

    # Weekly Rolling Average calculating of the relevant Daily stats
    df_bodyStats["Weight (Weekly)"] = df_bodyStats.weight.rolling(
        7, min_periods=1
    ).mean()
    df_bodyStats["Calories (Weekly)"] = (
        df_bodyStats.Calories(Actual).rolling(7, min_periods=1).mean()
    )

    return
