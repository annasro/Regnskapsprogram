import pandas as pd
from openpyxl import load_workbook

def makeDataFrame(header):
    df = pd.DataFrame(columns = header)
    return df

def addRowDataFrame(data,df):
    #data should be data = {Navn':name,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}}
    newRow = pd.Series(data)
    df = df.append(newRow, ignore_index = True)
    return df

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
 

 
