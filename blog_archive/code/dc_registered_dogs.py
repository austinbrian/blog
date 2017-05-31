'''Dataset of registered dogs in DC'''
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = '/Users/austinbrian/dev/blog/datasets/FOIA Request for Licensed Dogs By Zip 2015 to 2016 (Rabinowitz) 2016-FOIA-03763.xls'
dogs = pd.read_excel(dataset)

# This dataset is ugly; here is what's wrong with it:
# 1. Each entry is over three lines
# 2. There is a strange header
# 3. There is a total line for every zip code, which is inconvenient
# 4. Several of the header columns are merged cells

# Was able to fix several things in excel, then save as csv
fixed_csv = '/Users/austinbrian/dev/blog/datasets/dc_dog_data_2016.csv'
# this fixes: header, merged cells
# does not fix: three-line entries, total column
import csv
with open(fixed_csv,'rU') as d:
    reader = csv.reader(d)
    rows = [i for i in reader]

# first entry row prints with some weirdness
rows[0][0]=rows[0][0][3:]

# pull out the total rows
total_rows = []
data_rows = []
for i in rows:
    if i[2][:5] == "Total":
        total_rows.append(i)
    else:
        data_rows.append(i)

# turn them into lists of lists
datar = sum(data_rows,[]) # flatten data
n = 27 # there are 27 obs
data = [datar[i:i+n] for i in range(0, len(datar), n)]
print(data[:5])

# read in as pandas dataframe
dogs= pd.DataFrame(data[1:], columns=data[0])
dogs.drop('',axis=1) # drop empty columns

# clean up some of the columns
dogs.DOB = dogs.DOB.replace("",np.nan) # make blanks NaNs
dogs["DOB"] = pd.to_datetime(dogs["DOB"], format="%m/%d/%Y") #convert to datetime

# convert to datetime to calculate age
import datetime
today = datetime.datetime.today()

# from stackoverflow, single-line solution
# creates a new column, called dog_days, that includes rows where DOB is not null
dogs.loc[dogs['DOB'].notnull(), 'dog_days'] = (pd.to_datetime('now') - dogs['DOB']).dt.days
# turn that into years
dogs['dog_years'] = [round(i/365.,2) for i in dogs.dog_days]

# read in the total data
totalr = sum(total_rows,[]) # flatten data
n = 27 # there are 27 obs
total_data = [totalr[i:i+n] for i in range(0, len(totalr), n)]
print(total_data[:5])

# read in as pandas dataframe
alldogs= pd.DataFrame(total_data, columns=total_data[0])
# but I don't like it that want and want it flipped
alldogs = alldogs.transpose()
