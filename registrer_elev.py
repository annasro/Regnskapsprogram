from lib.lib1 import *

from lib.get_input import AskQuestion
from lib.registrer import registrer

path  = './testfolder/'
filename = 'testfile'

sheetname = 'elever'
path_excel = path + 'testfile'

filename = 'elever_' + filename 

name = 'elev'
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', str)

data =  {'Navn':[name], 'Email':[email], 'Telefonnummer':[phone]}

registrer(path, filename, path_excel, data, sheetname)