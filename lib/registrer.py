from .lib1 import *

from .write_files import saveToExcel


def registrer(path:str, filename:str, filename_excel:str,  data: dict, sheetname):
    
    if not os.path.exists(path):
        os.makedirs(path)

    df = pd.DataFrame.from_dict(data)

    #save to csv file, writes header if file has not yet been written to
    
    with open(path + filename + '.csv', 'a', newline='\n') as f:
       df.to_csv(f, header = (f.tell()==0), index = False)
    
    #ask terminal to save file to excel: 
    saveToExcel(df, sheetname, filename_excel)
    
    
    


