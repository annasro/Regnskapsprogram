import datetime
import pandas as pd
from lib import write_files as rw
from lib.get_input import GetInput


path = '../2021/excel/stray_2021.xlsx'
sheetname = 'hour_register'
header = ['Name','Hours', 'Date', 'Costumer']

#make DataFrame
df_header = rw.makeDataFrame(header)  #Dataframe with header only
file = rw.writeToHeaderExcel(df_header,path,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
df = pd.read_excel(path)

#input parameters
name = GetInput("Navn: ", str)
hours = GetInput('Antall timer: ', float)
costumer = GetInput('Kunde: ', str)
d = datetime.datetime.now()
date = d.strftime("%d.%m.%Y")


data =  {'Name':name, 'Hours':hours, 'Date': date, 'Costumer': costumer}

addrow_df = rw.addRowDataFrame(data,df_header)
print(addrow_df)
addrow_ex = rw.writeToBodyExcel(addrow_df,path,sheetname)
