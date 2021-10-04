from lib.lib1 import *
from lib.lib2 import *


sheetname = 'elever'
filename = 'elever_testfile'
filename_excel = path + 'testfile'

name = 'elev'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)

data =  {'Navn':[name], 'Email':[email], 'Telefonnummer':[phone]}

for k,v in data.items():
    print(f'{k}: {v}\n')

registrer(path, filename, filename_excel, data, sheetname)