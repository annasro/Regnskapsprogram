from lib.lib1 import *
from lib.lib2 import *


sheetname = 'elever'
filename = 'elever_' + filename 


name = 'elev'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)

data =  {'Navn':[name], 'Email':[email], 'Telefonnummer':[phone]}

for k,v in data.items():
    print(f'{k}: {v}\n')

registrer(path, filename, path_excel, data, sheetname)