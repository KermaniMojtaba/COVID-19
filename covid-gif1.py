# Section 1 - Importing Libraries
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import glob
import moviepy.editor as mpy

# Section 2 - Loading Data into Dataframes
df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv', parse_dates=['date'])
populations = pd.read_csv('http://www2.census.gov/programs-surveys/popest/datasets/2010-2019/national/totals/nst-est2019-alldata.csv?#', usecols=['NAME', 'POPESTIMATE2019'])

# Section 3 - Merging in Population Data & Calculating Rates
df = pd.merge(df, populations, how = 'left', left_on = 'state', right_on = 'NAME')
df['rate'] = df['cases'] / df['POPESTIMATE2019'] * 100000