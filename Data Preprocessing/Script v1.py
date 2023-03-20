####### Placeholder

##Import libs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer


## Import data files

crm = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/crm.csv')
mkt = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/mkt.csv')
sales = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/sales.csv')


## High level data
sales.head(), crm.head(), mkt.head()

sales.info(), crm.info(),mkt.head()

## Checking duplicated values
mkt[mkt.duplicated()], crm[crm.duplicated()], mkt[mkt.duplicated()]

## Dropping duplicated values and then dataframe checking
sales_dedup = sales.drop_duplicates() 
crm_dedup = crm.drop_duplicated()
mkt_dedup = mkt.drop_duplicated()

sales_dedup.info()
crm_dedup.info()
mkt_dedup.info()

## Setting Customer as our Index Key
sales_dedup.set_index('CustomerID', inplace = True)  ## Changes are permanent since we used the inplace
## This is an equivalent df = df.set_index('Custid')
crm_dedup.set_index('CustomerID', inplace = True)
mkt_dedup.set_index('CustomerID', inplace = True)


## MissClassifications
crm['Education'].value_counts()
crm['Education'] = crm['Education'].str.capitalize()


crm['Marital_Status'] = crm['Marital_Status'].str.capitalize()

## Create Age Varible from Birthyear
from datetime import datetime

time = datetime.now()
crm['Age'] = time.year - df['Birthyear']

# Check for inconsistencies of children and Age

unique_names = crm.loc[df['Children_6to18'] >0, 'Birthyear'].unique()
unique_names = crm.loc[df['Kid_Younger6'] >0, 'Birthyear'].unique()

#Check for inconsistencies of Marital_Status and Age
for status in crm['Marital_Status'].unique(): ## for each unique status in Marital Status
    unique_ages = np.sort(crm.loc[crm['Marital_Status'] == status, 'Age'].unique()) #filters the crm dataframe to only include rows where the 'Marital_Status' column matches the current status value, find the unique value in Age and sort them
    print(f"Unique ages for marital status {status}: {unique_ages}") #print the current marital status value and the corresponding unique ages 
    
    
### Merging the dfs

spice_aley = pd.merge(pd.merge(crm, mkt, on='CustomerID'), sales, on='CustomerID')

