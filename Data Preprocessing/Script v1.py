####### Placeholder

##Import libs

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer


## Import data files

crm = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/crm.csv?token=GHSAT0AAAAAACAH7ERLXCC56XR3W4JTPOQWZAXTZJQ')
mkt = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/mkt.csv?token=GHSAT0AAAAAACAH7ERKOIVF5OEX6G72NKWCZAXTYTA')
sales = pd.read_csv('https://raw.githubusercontent.com/EFSA-Jedi-Group/Data-Science-and-ML/main/Data/sales.csv?token=GHSAT0AAAAAACAH7ERL6GW2GDL4AUJTPFMMZAXTU5Q')
