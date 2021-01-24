import pandas as pd
from writeToFromFiles import*
import inquirer


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
header = ['Navn','Varenummer','Produkttype', 'Inntektskonto','Enhetspris','MVA-Type' 'Varebeholdning','Merknad','Belop_eks_mva','Mvakode','Kontonummer',]

#itemName = 'Anna'
#VAT_code = 'HØY'
amount = 50000
revenue_account = 3220
price = 247.5
b_accountno = 50
quantity = 50
product_no = 1076
product_type = {'Vare(videresalg)','Vare(egenprodusert)','Tjeneste', 'Annet'}


#make Dataframe
df_header = makeDataFrame(header)  #Dataframe with header only
file_excel = writeToHeaderExcel(df_header,pathEXCEL,sheetname) #write header to excelfile- needs to be before adding rows to dataframe
df = pd.read_excel(pathEXCEL)

itemName = getInput(" Produktnavn/beskrivelse: ",str)
VAT_code =  getInput('Mvasats(høy, middels, lav, inten, unntatt):', str)
VAT_codes = {'Navn':itemName,'Belop_eks_mva':amount, 'Mvakode':VAT_code, 'Kontonummer':b_accountno,'Antall':quantity, 'Varenummer':product_no}



if (VAT_code == 'HØY'):
    Value = 0.25
elif (VAT_code == 'MIDDELS'):
    Value == 0.15
elif (VAT_code == 'LAV'):
    Value == 0.12
elif (VAT_code == 'INGEN'):
    Value = 0.0
elif (VAT_code == 'FRITATT'):
    Value == 0.0
else:
    VAT_code == 0.25

#data = [(itemName , amount , VAT_code , b_accountno , quantity, product_no)]
#adding row to DataFrame

header = ['Navn','Varenummer','Produkttype', 'Inntektskonto','Enhetspris','MVA-Type' 'Varebeholdning','Merknad','Belop_eks_mva','Mvakode','Kontonummer',]

data = {'Navn':itemName, 'Varenummer':product_no,'Produkttype':product_type,'Inntektskonto':revenue_account,
        'Enhetspris':price,'Varebeholdning':inventory,'Merknad':note,
        'Belop_eks_mva':amount,'Mvakode':VAT_code,'Kontonummer':b_accountno,}
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
