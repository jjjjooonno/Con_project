from pandas import *
import numpy as np
data = read_excel('cleaned_data.xlsx')
data['age'] = to_numeric(data['age'],'coerce').fillna(999).astype(np.int64)
# data['date'] = to_datetime(data['date'],'coerce').fillna(999)
# data['injury_date'] = to_datetime(data['injury_date'])
for i in range(0,len(data.index)):
    if data.iloc[i,0] > 100 and data.iloc[i,0] < 900:
        data.iloc[i,0] = data.iloc[i,0] - 100
print(data['age'].describe())