from lib.lib1 import *

from lib.get_input import AskQuestion
from lib.registrer import registrer


path  = "G:\Min disk\Enkeltpersonsforetak\Regnskap\\2021\excel\\"
filename = 'stray_2021_new'

path_excel = path + filename

sheetname = 'elever'
filename = 'elever_' + filename 

name = AskQuestion('Navn på elev: ', str)
email = AskQuestion('Email: ', str)
phone = AskQuestion('Telefonnummer: ', int)

data =  {'Navn':[name], 'Email':[email], 'Telefonnummer':[phone]}

registrer(path, filename, path_excel, data, sheetname)