from lib.lib1 import *
from lib.lib2 import *

sheetname = 'kunder'
filename = 'elever_testfile'
filename_excel = 'testfile'

name = 'kunde'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)
adress = AskQuestion('Adresse: ', str)
postcode = AskQuestion('Postnummer + by')

costumer_number = 1

data =  {'Kunde':[name], 'Email':[email], 'Telefonnummer':[phone], 'Adresse':[adress], 'Postnummer':[postcode], 'Kundenummer':[costumer_number]}

for k,v in data.items():
    print(f'{k}: {v}\n')

registrer(path, filename, filename_excel, data, sheetname)