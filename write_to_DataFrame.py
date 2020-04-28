import pandas as pd
from openpyxl import load_workbook

def getInput(text, type_ = None, min_=None, max_= None, range_=None):

    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError('min_ must be less or equal to max_.')
    while True:
        Value = input(text)
        if type_ is not None:
            try:
                Value = type_(Value)
            except ValueError:
                print('Input type must be {0}.'.format(type_.__name__))
                continue
        if max_ is not None and Value > max_:
             print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and Value < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and Value not in range_:
            if isinstance(range_, range):
                template = 'Input must be between {0.start} and {0.stop}.'
                print(template.format(range_))
            else:
                template = 'Input must be {0}.'
                if len(range_)== 1:
                    print(template.formate(*range_))
                else:
                     print(template.format(" or ".join((", ".join(map(str,range_[:-1])), str(range_[-1])))))
        else:
            return Value

def makeDataFrame(header):
    df = pd.DataFrame(columns = header)
    return df

def addRowDataFrame(data,df):
    #data should be data = {Navn':name,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}}
    newRow = pd.Series(data)
    df = df.append(newRow, ignore_index = True)
    return df

def writeToHeaderExcel(df,path,sheetname):
    writer, reader = writeToExcel(df,path,sheetname)
    df.to_excel(writer,sheet_name = sheetname,index=False,header=True) #make header
    writer.save()
    writer.close()
    return df

def writeToBodyExcel(df,path,sheetname):
    writer, reader = writeToExcel(df,path,sheetname)
    df.to_excel(writer,sheet_name = sheetname ,index=False,header=False,startrow=len(reader)+1) #add rows
    writer.save()
    writer.close()
    return df

def writeToExcel(df,path,sheetname):
    with pd.ExcelWriter(path,engine='openpyxl',mode = 'a') as writer:
        book = load_workbook(path) #open excelfile
        writer.book = book                 #workbook
        reader = pd.read_excel(path)        #reading excelfile
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets) #copying worksheet
    return writer, reader


itemName = 'Anna'
amount = 1000
VAT_code = 'HØY'
b_accountno = 123
quantity = 2
product_no = 100

#Create a DataFrame object
path = './data/excel/test.xlsx'
sheetname = 'Ark1'
header = ['Navn', 'Belop_eks_mva','Mvakode','Kontonummer','Antall','Varenummer']
df = makeDataFrame(header)  #Dataframe with header only
df = writeToHeaderExcel(df,path,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
#data = [(itemName , amount , VAT_code , b_accountno , quantity, product_no)]
#adding row to DataFrame
data = {'Navn':itemName,'Belop_eks_mva':amount, 'Mvakode':VAT_code, 'Kontonummer':b_accountno,'Antall':quantity, 'Varenummer':product_no}
df = addRowDataFrame(data, df)
df = writeToBodyExcel(df,path,sheetname)



'''

while True:
    if any(df.Navn == ItemName):
        print('Produktet finnes allerede \n')
        print(df.loc[df.Navn == ItemName])         #gives relevant rows
        print(df.loc[df.Navn == ItemName].index)   #Gives relevant row names
    elif any(df.Varenummer == product_no):
        print('Produktnummeret finnes allerede \n')
        print(df.loc[df.Varenummer == product_no])         #gives relevant rows
        print(df.loc[df.Varenummer == product_no].index)   #Gives relevant row names
    else:
        break
'''
