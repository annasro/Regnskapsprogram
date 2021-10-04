from lib.lib1 import *
from lib.lib2 import *

from lib.get_input import GetInput
from lib.str2bool import str2bool
from lib.write_files import writeToBodyExcel, writeToHeaderExcel, writeToExcel

def registrer(path:str, filename:str, filename_excel:str,  data: dict, sheetname):
    
    if not os.path.exists(path):
        os.makedirs(path)

    df = pd.DataFrame.from_dict(data)
    
    with open( path + filename + '.csv', 'a') as f:
        df.to_csv(f, mode='a', header=f.tell()==0)
    
    #ask terminal to save file to excel: 
    SaveToExcel = GetInput('Vil du lagre data til excel [y/n]? ', str)
    if str2bool(SaveToExcel) == True:
        header = list(df.columns)
        df_header = pd.DataFrame(columns = header)
        writeToHeaderExcel(df_header, filename_excel + '.xlsx',sheetname) #write header to excelfile- needs to be before adding rows to dataframe
        writeToBodyExcel(df, filename_excel + '.xlsx',sheetname)
        
    


