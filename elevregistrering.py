import datetime
import pandas as pd
from lib import write_files as rw
from lib.get_input import GetInput

path = './excel/stray_2021.xlsx'
sheetname = 'Students'
header = ['Name','Mail', 'Phone']

df_header = rw.makeDataFrame(header)  #Dataframe with header only
file = rw.writeToHeaderExcel(df_header,path,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
df = pd.read_excel(path)


#input parameters
name = GetInput("Navn: ", str)
mail = GetInput('Mail: ', str)
phone = GetInput('Phone: ', int)

data =  {'Name':name, 'Mail':mail, 'Phone': phone}

addrow_df = rw.addRowDataFrame(data,df_header)
print(addrow_df)
addrow_ex = rw.writeToBodyExcel(addrow_df,path,sheetname)


