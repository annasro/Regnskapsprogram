import pandas as pd

name, amount, VAT_code, b_accountno,quantity,product_no = []
columns = ['Navn', 'Belop_eks_mva','Mvakode','Konto','Antall','Varenummer']
data = {'Navn':name,'Belop_eks_mva':amount,
        'Mvakode': VAT_code,'Konto':b_accountno,
        'Antall':quantity,'Varenummer':product_no}

def getInput(promt,type = None, min_=None, max_= None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError('min_ must be less or equal to max_.')
    while True:
        value = input(promt)
        if type_ is not None:
            try:
                value = type_(value)
            except ValueError:
                print('Input type must be {0}.'.format(type_.__name__))
                continue
        if max_ is not None and value > max_:
             print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and value < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and value not in range_:
            if isinstance(range_, range):
                template = 'Input must be between {0.start} and {0.stop}.'
                print(template.format(range_))
            else:
                template = 'Input must be {0}.'
                if len(range_)== 1:
                    print(template.formate(*range_))
                else pprint(template.format(" or ".join((", ".join(map(str,
                                                                     range_[:-1])),
                                                       str(range_[-1])))))
        if any(df.name == value):
            print('Produktet finnes allerede \n')
            print(df.loc[df.name == input])         #gives relevant rows
            print(df.loc[df.name == input].index)   #Gives relevant row names
            continue

            '''
        if (value = 'HØY'):
            value = 0.25
        elif (value = 'MIDDELS'):
            value = 0.15
        elif (value = 'LAV'):
            value = 0.12
        elif (value = 'INGEN'):
            value = 0.0
        elif (value = 'FRITATT'):
            value = 0.0
        else:
            value = 0.25
            '''

        else:
            return value


def input():
        #df.lookup([0,2,4,6], ['B','C','A',D]) #gives array with index 0 from colum B etc
        #input error

    #ask for amount
    #ask for VAT_code - if none set to 25
    #ask for quantity
    #add number (totalt number of rows + 1)

itemName = getInput('Produktnavn/beskrivelse: ')
amount = getInput('Pris per stk: ',float)
VAT_code =  getInput('Mvasats(høy, middels, lav, inten, unntatt):')
#b_accountno = b_accountno #import
quantity = getInput('Antall solgt: ', int)
#itemNo = number of rows + 1


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

def makeDataFrame(data):
    return df = pd.DataFrame(data)

def addRowDataFrame(data,df):
    #data should be data = {Navn':name,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}}
    new_row = pd.Series(data)
    df = df.append(new_row, ignore_index = True)

def makeExcelFile(df):
    df.to_excel(path,sheetname,index = True)


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
