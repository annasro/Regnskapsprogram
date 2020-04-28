import pandas as pd

def makeDataFrame(data,columns):
    df = pd.DataFrame(data)
    df.columns  = columns
    return df

def addRowDataFrame(data,df):
    #data should be data = {Navn':name,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}}
    newRow = pd.Series(data)
    print(newRow)
    df = df.append(newRow, ignore_index = True)
    return df

def makeExcelFile(df, path, sheetname):
    df.to_excel(path,sheetname,index = True)


itemName = 'Anna'
amount = '10'
VAT_code = 'HØY'
b_accountno = '123'
quantity = '2'
product_no = '1'

#Create a DataFrame object
columns = ['Navn', 'Belop_eks_mva','Mvakode','Kontonummer','Antall','Varenummer']
data = [(itemName , amount , VAT_code , b_accountno , quantity, product_no)]
df = makeDataFrame(data,columns)

#adding row to DataFrame
data = {'Navn':itemName,'Belop_eks_mva':amount, 'Mvakode':VAT_code, 'Kontonummer':b_accountno,'Antall':quantity, 'Varenummer':product_no}
df = addRowDataFrame(data, df)


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
