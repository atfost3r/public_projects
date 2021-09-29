#!python3

# progress.py - This subroutine is to calculate how I am progressing this will
#               read in data and crunch metrics on how I am doing
#


from datetime import datetime
import pandas as pd

def progressDaily():
    # read in the csv containing all my body data
    df_dailyBodyStats = pd.read_csv("fitness_tracker/databases/dailyBodyStats.csv", encoding="utf-8")
    df_dailyBodyStats['weight_delta']   =  df_dailyBodyStats['weight'].diff()
    df_dailyBodyStats['calories_delta'] =  df_dailyBodyStats['calories_goal'] - df_dailyBodyStats['calories_actual']    
    df_dailyBodyStats['protein_delta']  =  df_dailyBodyStats['protein_goal'] - df_dailyBodyStats['protein_actual']
    df_dailyBodyStats['carbs_delta']    =  df_dailyBodyStats['carbs_goal'] - df_dailyBodyStats['carbs_actual']
    df_dailyBodyStats['fat_delta']      =  df_dailyBodyStats['fat_goal'] - df_dailyBodyStats['fat_actual']
    #Save daily progress stats
    df_dailyBodyStats.to_csv("fitness_tracker/databases/dailyProgressStats.csv", encoding='utf-8') 
    return

def progressWeekly(date):
    # read in the csv containing all my body data
    df_bodyStats = pd.read_csv("fitness_tracker/databases/dailyBodyStats.csv", encoding="utf-8")

    # Weekly Rolling Average calculating of the relevant Daily stats
    df_bodyStats["weight_weekly"] = df_bodyStats.weight.rolling(
        7, min_periods=1
    ).mean()
    df_bodyStats["calories_weekly"] = (
        df_bodyStats.calories_actual.rolling(7, min_periods=1).mean()
    )
    print(df_bodyStats.head())
    df_bodyStats.to_csv("fitness_tracker/databases/weeklyProgressStats.csv", mode='a', header=FALSE,encoding='utf-8') 
    return

#progressWeekly(datetime.now())