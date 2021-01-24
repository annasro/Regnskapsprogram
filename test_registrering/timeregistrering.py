import datetime
import pandas as pd
from lib import write_files as rw
from lib.get_input import GetInput
from lib import let_user_pick as pick

path = './excel/test.xlsx'
sheetname = 'timeregisrering'
header = ['Navn','Timer', 'Dato', 'Kunde']

#make DataFrame
df_header = rw.makeDataFrame(header)  #Dataframe with header only
file = rw.writeToHeaderExcel(df_header,path,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
df = pd.read_excel(path)

#input parameters
name = GetInput("Navn: ", df, str)
hours = GetInput('Antall timer: ', df, float)
costumer = GetInput('Kunde: ', df, str)
d = datetime.datetime.now()
date = d.strftime("%d.%m.%Y")


data =  {'Navn':name, 'Timer':hours, 'Dato': date, 'Kunde': costumer}

addrow_df = rw.addRowDataFrame(data,df_header)
print(addrow_df)
#addrow_ex = rw.writeToBodyExcel(addrow_df,path,sheetname)
