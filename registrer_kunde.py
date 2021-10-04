from lib.lib1 import *

from lib.get_input import AskQuestion
from lib.registrer import registrer

path  = './testfolder/'
filename = 'testfile'

path_excel = path + 'testfile'
sheetname = 'kunder'

filename = 'kunder_' + filename

name = 'kunde'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)
adress = AskQuestion('Adresse: ', str)
postcode = AskQuestion('Postnummer + by: ', str)

costumer_number = 1

data =  {'Kunde':[name], 'Email':[email], 'Telefonnummer':[phone], 'Adresse':[adress], 'Postnummer':[postcode], 'Kundenummer':[costumer_number]}

registrer(path, filename, path_excel, data, sheetname)