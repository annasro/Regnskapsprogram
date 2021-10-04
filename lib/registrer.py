from lib.lib1 import *
from lib.lib2 import *

from lib.get_input import GetInput
from lib.str2bool import str2bool
from lib.write_files import writeToBodyExcel, writeToHeaderExcel, writeToExcel

def registrer(path:str, filename:str, filename_excel:str,  data: dict, sheetname):
    
    #if not os.path.exists(path):
        #os.makedirs(path)

    df = pd.DataFrame.from_dict(data)

    #if file does not exsist, create csv file from df and use keys from data dict as header
    if not os.path.isfile(filename + '.csv'):
        df.to_csv(path + filename + '.csv', header = data.items(), mode = 'a+', index = False)
    else: # else it exists so append without writing the header
        df.to_csv(path + filename + '.csv', mode = 'a+', header=False, index = False)

    
    #ask terminal to save file to excel: 
    SaveToExcel = GetInput('Vil du lagre data til excel [y/n]? ', str)
    if str2bool(SaveToExcel) == True:
        header = list(df.columns)
        df_header = pd.DataFrame(columns = header)
        writeToHeaderExcel(df_header, filename_excel + '.xlsx',sheetname) #write header to excelfile- needs to be before adding rows to dataframe
        writeToBodyExcel(df, filename_excel + '.xlsx',sheetname)
        
    


