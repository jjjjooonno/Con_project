from pandas import *
import sys

dt = read_excel(sys.path[1]+'/cleaned_data0305.xlsx')
print(dt['gender'].describe())
print(dt['wound'].describe() )
wl = unique(dt['wound'])
wound = DataFrame({'wound_var' : wl})
wound.to_excel('wound_vars.xlsx')