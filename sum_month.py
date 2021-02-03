import pandas as pd

path = './excel/test.xlsx'
sheetname = 'hour_register'

df = pd.read_excel(path, sheet_name = sheetname).drop(['Costumer'], axis = 1)
df['Date'] = pd.to_datetime(df['Date'])
a = df.groupby([df['Date'].dt.month]).sum()

print(a)
b = a._get_value(1, 'Hours')

print(b)


#s1 = df.groupby(pd.to_datetime(df.Date).dt.month).sum()
#print(s1)
