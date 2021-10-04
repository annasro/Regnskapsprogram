from lib.lib1 import *
from lib.lib2 import *

sheetname = 'kunder'
filename = 'kunder_' + filename

name = 'kunde'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)
adress = AskQuestion('Adresse: ', str)
postcode = AskQuestion('Postnummer + by')

costumer_number = 1

data =  {'Kunde':[name], 'Email':[email], 'Telefonnummer':[phone], 'Adresse':[adress], 'Postnummer':[postcode], 'Kundenummer':[costumer_number]}

for k,v in data.items():
    print(f'{k}: {v}\n')

registrer(path, filename, path_excel, data, sheetname)