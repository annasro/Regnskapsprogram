import pandas as pd


def makeDict(columns):
    Dict = {listKey: [] for listKey in columns}
    return Dict

def makeDataFrame(data):
    df = pd.DataFrame(data)
    return df

def addRowDataFrame(data,df):
    #data should be data = {Navn':name,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}}
    new_row = pd.Series(data)
    df = df.append(new_row, ignore_index = True)
    return df


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
'''
itemName = getInput(" Produktnavn/beskrivelse: ",str)
amount = getInput('Pris per stk: ',float)
VAT_code =  getInput('Mvasats(høy, middels, lav, inten, unntatt):', str)
b_accountno = b_accountno #import
quantity = getInput('Antall solgt: ', int)
itemNo = number of rows + 1
'''

columns = ['Navn', 'Belop_eks_mva','Mvakode','Konto','Antall','Varenummer']
myDict = makeDict(columns)
df = makeDataFrame(myDict)
Itemname = 'Anna'
amount = 10
VAT_code = 'HØY'
b_accountno = 123
quantity = 2
product_no = 1
data = {'Navn':Itemname,'Belop_eks_mva':amount,'Mvakode': VAT_code,'Konto':b_accountno,'Antall':quantity,'Varenummer':product_no}
newRow = addRowDataFrame(data, df)


'''
if any(df.Navn == itemName):
    print('Produktet finnes allerede \n')
    print(df.loc[df.name == input])         #gives relevant rows
    print(df.loc[df.name == input].index)   #Gives relevant row names
'''



'''
if (Value = 'HØY'):
    Value = 0.25
elif (Value = 'MIDDELS'):
    Value = 0.15
elif (Value = 'LAV'):
    Value = 0.12
elif (Value = 'INGEN'):
    Value = 0.0
elif (Value = 'FRITATT'):
    Value = 0.0
else:
    Value = 0.25
    '''
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
