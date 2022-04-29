import pandas as pd
import numpy as np
import datetime as dt
import pytz

raw = "rawdata.xlsx"

df = pd.read_excel(raw)

# change data to a type of datetime 
df['time'] = pd.to_datetime(df["time"], utc = True)




