from pandas import *
from xlrd import XLRDError
datas = []

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
dt = datas[5]
for i in datas:
    print(i.columns.values)
    print(i.head(1))