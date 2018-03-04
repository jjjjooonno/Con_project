from pandas import *
from xlrd import XLRDError
import numpy as np
datas = []
date = []
gender = []
age = []
item_s = []
item_m = []
item_l = []
treat_time = []
wound = []
injury = []
place = []
injury_date = []
madein = []


for i in [2013,2014,2015,2016,2017]:
    for j in [1,2,3,4]:
        filename = str(i)+str(j)
        try:
            dt = read_csv('/Users/joono/GoogleDrive/SKKU/BOAZ/10+11기/BOAZ_Vis/Project/download/'+filename+'.csv', encoding = 'euc-kr')
            datas.append(dt)
        except FileNotFoundError:
            try:
                dt = read_excel(
                    '/Users/joono/GoogleDrive/SKKU/BOAZ/10+11기/BOAZ_Vis/Project/download/' + filename + '.xlsx')
                datas.append(dt)
            except FileNotFoundError:
                continue
        except XLRDError:
            dt = read_excel(
                '/Users/joono/GoogleDrive/SKKU/BOAZ/10+11기/BOAZ_Vis/Project/download/' + filename + '.xlsx')
            datas.append(dt)
for i in range(0,len(datas)):
    datas[i] = datas[i].fillna(210)
for data in datas[:5]:
    for k in range(0,len(data.index)):
        date.append(data.iloc[k,0])
        gender.append(data.iloc[k,1])
        if data.iloc[k, 2] == '210':
            age.append('unknown')
        else:
            age.append(int(data.iloc[k, 2]))
        item_s.append(data.iloc[k, 4])
        item_m.append(data.iloc[k, 18])
        item_l.append(data.iloc[k, 17])
        treat_time.append(data.iloc[k, 8])
        wound.append(data.iloc[k, 10])
        injury.append(data.iloc[k, 12])
        place.append(data.iloc[k, 14])
        injury_date.append(data.iloc[k, 16])
        madein.append(data.iloc[k,7])
for l in range(len(datas[5].index)):
    date.append(datas[5].iloc[l, 0])
    gender.append(datas[5].iloc[l, 1])
    age.append(int(datas[5].iloc[l, 2]) - 100)
    item_s.append(datas[5].iloc[l, 3])
    item_m.append(datas[5].iloc[l, 11])
    item_l.append(datas[5].iloc[l, 10])
    treat_time.append(datas[5].iloc[l, 5])
    wound.append(datas[5].iloc[l, 6])
    injury.append(datas[5].iloc[l, 7])
    place.append(datas[5].iloc[l, 8])
    injury_date.append(datas[5].iloc[l, 9])
    madein.append(datas[5].iloc[l, 7])
for data in datas[6:10]:
    for k in range(0, len(data.index)):
        date.append(data.iloc[k, 0])
        gender.append(data.iloc[k, 1])
        age.append(int(data.iloc[k, 2]) - 100)
        item_s.append(data.iloc[k, 3])
        item_m.append(data.iloc[k, 11])
        item_l.append(data.iloc[k, 10])
        treat_time.append(data.iloc[k, 5])
        wound.append(data.iloc[k, 6])
        injury.append(data.iloc[k, 7])
        place.append(data.iloc[k, 8])
        injury_date.append(data.iloc[k, 9])
        madein.append(data.iloc[k,4])
# [‘접수번호' '접수일' '위해자연령' '위해자성별' '발생일자' '치료기간' '품목대분류' '품목중분류' '품목소분류' '원산지' '위험및위해원인' '위해부위' '발생장소']
for data in datas[10:13]:
    for k in range(0, len(data.index)):
        date.append(data.iloc[k, 1])
        gender.append(data.iloc[k,3])
        if data.iloc[k,2] == '210':
            age.append('unknown')
        else:
            age.append(int(data.iloc[k,2]))
        item_s.append(data.iloc[k, 8])
        item_m.append(data.iloc[k, 7])
        item_l.append(data.iloc[k, 6])
        treat_time.append(data.iloc[k, 5])
        wound.append(data.iloc[k, 11])
        injury.append(data.iloc[k, 10])
        place.append(data.iloc[k, 12])
        injury_date.append(data.iloc[k, 4])
        madein.append(data.iloc[k,9])
# 13[‘번호' '접수일' '위해자연령' '성별' '발생일자' '치료기간' '품목대분류' '품목중분류' '품목소분류' '위험및위해원인' '위해증상 대분류' '위해증상 소분류' '발생장소']
for data in datas[13:15]:
    for k in range(0, len(data.index)):
        date.append(data.iloc[k, 1])
        gender.append(data.iloc[k,3])
        if data.iloc[k,2] == '210':
            age.append('999')
        else:
            age.append(int(data.iloc[k,2]))
        item_s.append(data.iloc[k, 8])
        item_m.append(data.iloc[k, 7])
        item_l.append(data.iloc[k, 6])
        treat_time.append(data.iloc[k, 5])
        wound.append(data.iloc[k, 11])
        injury.append(data.iloc[k, 9])
        place.append(data.iloc[k, 12])
        injury_date.append(data.iloc[k, 4])
        madein.append('999')
# [‘접수번호' '접수일' '위해자연령' '위해자성별' '발생일자' '치료기간' '품목대분류' '품목중분류' '품목소분류' '원산지' '위험및위해원인' '위해부위' '발생장소']
for data in datas[15:]:
    for k in range(0, len(data.index)):
        date.append(data.iloc[k, 1])
        gender.append(data.iloc[k, 3])
        if data.iloc[k, 2] == '210':
            age.append('999')
        else:
            age.append(int(data.iloc[k, 2]))
        item_s.append(data.iloc[k, 8])
        item_m.append(data.iloc[k, 7])
        item_l.append(data.iloc[k, 6])
        treat_time.append(data.iloc[k, 5])
        wound.append(data.iloc[k, 11])
        injury.append(data.iloc[k, 10])
        place.append(data.iloc[k, 12])
        injury_date.append(data.iloc[k, 4])
        madein.append(data.iloc[k,9])
final_dataset = DataFrame({'date' : date,
'gender' : gender,
'age' : age,
'item_s' : item_s,
'item_m' : item_m,
'item_l' : item_l,
'treat_time' : treat_time,
'wound' : wound,
'injury' : injury,
'place' : place,
'injury_date' : injury_date,
'madein' : madein})
final_dataset.to_excel('cleaned_data.xlsx')