
from .lib1 import *
from .get_input import GetInput
from .str2bool import str2bool




def writeToHeaderExcel(df,path,sheetname):
    writer = writeToExcel(path)
    headerexcel = df.to_excel(writer, sheet_name = sheetname, index = False, header = True) #make header
    writer.save()
    
    return headerexcel

def writeToBodyExcel(df,path,sheetname):
    writer = writeToExcel(path)
    reader = pd.read_excel(path, sheetname)        #reading excelfile
    bodyexcel = df.to_excel(writer, sheet_name = sheetname, 
                            index=False, header = False,
                            startrow = len(reader) + 1) #add rows
    writer.save()
   
    return bodyexcel

def writeToExcel(path):
    book = load_workbook(path)
    writer = pd.ExcelWriter(path, engine = 'openpyxl', mode ='r+')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    return writer

def saveToExcel(df, sheetname, path_excel):
    SaveToExcel = GetInput('Vil du lagre data til excel [y/n]? ', str)
    
    if str2bool(SaveToExcel) == True:
        header = list(df.columns)
        df_header = pd.DataFrame(columns = header)
        writeToHeaderExcel(df_header, path_excel + '.xlsx',sheetname) #write header to excelfile- needs to be before adding rows to dataframe
        writeToBodyExcel(df, path_excel + '.xlsx',sheetname)



 

 
