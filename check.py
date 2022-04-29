import pandas as pd
import numpy as np
import datetime as dt
import pytz

raw = "../data/rawdata.xlsx"

df = pd.read_excel(raw)

# change data to a type of datetime 
df['time'] = pd.to_datetime(df["time"], utc = True)

# how many total missing values in VTWS_AVG
missing = sum(df["VTWS_AVG"].isnull())

# adding erroneous column 
df["data qc flag VTWS_AVG"] = np.where(df["VTWS_AVG"].isnull(), "Erroneous", "")

# checking how many erroneous values there are compared to missing 
# (should be a true logical statement as there are just as many missing as Erroneous)
missing == sum(df["data qc flag VTWS_AVG"] == "Erroneous")

# in order to create a new excell file with our changes we need to eliminate the 
# timezone or UTC as creating an excel file does not like having one.
df['time'] = pd.to_datetime(df["time"])
df['time'] = df['time'].dt.tz_localize(None)

df.to_excel("../data/finaldata.xlsx", index = False)



