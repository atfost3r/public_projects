#!python3

# progress.py - This subroutine is to calculate how I am progressing this will 
#               read in data and crunch metrics on how I am doing 
# 

from os import wait
import pandas as pd

# read in the csv containing all my body data
df_bodyStats = pd.read_csv('databases/bodyStats.csv', encoding='utf-8')

print(df_bodyStats.head())


df_bodyStats['SMA_10'] = df_bodyStats.Weight.rolling(7, min_periods=1).mean()