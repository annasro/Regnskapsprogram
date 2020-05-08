import pandas as pd
from writeToFromFiles import*

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

        if any(df.Navn == Value) or any(df.product_no == Value):
            print('Produktet finnes allerede \n')
            print(df.loc[df.Navn == Value])         #gives relevant rows
            print(df.loc[df.Navn == Value].index)   #Gives relevant row names
            print('Prøv igjen\n')



        else:
            return Value


'''
amount = getInput('Pris per stk: ',float)

b_accountno = b_accountno #import
quantity = getInput('Antall solgt: ', int)
itemNo = number of rows + 1
'''

#inputs
pathEXCEL = r'./data/excel/test.xlsx'
pathCSV = r'./data/CSV/test.csv'
sheetname = 'Ark1'
header = ['Navn', 'Belop_eks_mva','Mvakode','Kontonummer','Antall','Varenummer']

#itemName = 'Anna'
#VAT_code = 'HØY'
amount = 50000
b_accountno = 50
quantity = 50
product_no = 1076

#make Dataframe
df_header = makeDataFrame(header)  #Dataframe with header only
file_excel = writeToHeaderExcel(df_header,pathEXCEL,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
df = pd.read_excel(pathEXCEL)

itemName = getInput(" Produktnavn/beskrivelse: ",str)
VAT_code =  getInput('Mvasats(høy, middels, lav, inten, unntatt):', str)
VAT_codes = {'Navn':itemName,'Belop_eks_mva':amount, 'Mvakode':VAT_code, 'Kontonummer':b_accountno,'Antall':quantity, 'Varenummer':product_no}



if (VAT_code == 'HØY'):
    Value = 0.25
elif (Value == 'MIDDELS'):
    Value == 0.15
elif (Value == 'LAV'):
    Value == 0.12
elif (Value == 'INGEN'):
    Value = 0.0
elif (Value == 'FRITATT'):
    Value == 0.0
else:
    Value == 0.25

#data = [(itemName , amount , VAT_code , b_accountno , quantity, product_no)]
#adding row to DataFrame

data = {'Navn':itemName,'Belop_eks_mva':amount, 'Mvakode':VAT_code, 'Kontonummer':b_accountno,'Antall':quantity, 'Varenummer':product_no}
df = addRowDataFrame(data, df_header) #add row to dataframe


file_excel = writeToBodyExcel(df,pathEXCEL,sheetname)
file_csv = writeToCSV(pathEXCEL, pathCSV)

'''
#Format imports - filter
#wont matter if cap or not.
#remove spacings
replies = map(input, prompts)
lowercased_replies = map(str.lower, replies)
stripped_replies = map(str.strip, lowercased_replies)
valid_response = next(filter(fruits.__contains__, stripped_replies))
print(valid_response)
from itertools import chain, repeat

from lz.functional import compose

fruits = {'apple', 'orange', 'peach'}
prompts = chain(["Enter a fruit: "], repeat("I don't know this one! Try again: "))
replies = map(input, prompts)
process = compose(str.strip, str.lower)  # you can add more functions here
processed_replies = map(process, replies)
valid_response = next(filter(fruits.__contains__, processed_replies))
print(valid_response)
'''

'''
#bestemme hva som skjer med tomme/manglende verdier.
(df.style
   .set_na_rep("FAIL")
   .format(None, na_rep="PASS", subset=["D"])
   .highlight_null("yellow"))

#hide index, columns:
df.style.hide_columns(['C','D'])
df.style.hide_index()


    quantity = data.Antall
    mylist = []
    myset = set()
    for item in ...:
        if item not in myset:
            mylist.append(item)
            myset.add(item)
    product_no = data.Varenummer

    return
'''
