import datetime
import pandas as pd
import pandas_datareader as dr

import write_files as rw
from get_input import GetInput

def register ():
    header = ['name', 'age', 'city']
    df_header = rw.makeDataFrame(header)  #Dataframe with header only
    #file = rw.writeToHeaderExcel(df_header,path,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
    #df = pd.read_excel(path)

    print(df_header)

    #make all header titles to variables
    #use GetInput to set value to variable
    #make dict with the values of the variables
    #make dataframe out of dict
    df_dict = {}
    df_dict['parameter 1'] = GetInput("{parameter 1}", str)
    GetInput

    for var in header:
        df_dict[var] = pd.DataFrame()
        #df_dict[var] = dr.data.get_data_yahoo(var, start, end)
   


register()