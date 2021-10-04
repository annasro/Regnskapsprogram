from lib.lib1 import*
from lib.lib2 import *


sheetname = 'timer'
filename = 'timer_testfile'
filename_excel = path + 'testfile'

hours = AskQuestion('Hvor hvor mange timer underviste du? ', str)

name = 'Anna'
costumer = 1

d = datetime.datetime.now()
date = d.strftime("%d.%m.%Y")

data =  {'Name':[name], 'Hours':[hours], 'Date': [date], 'Kundenummer': [costumer]}
registrer(path, filename, filename_excel, data, sheetname)

'''
#input parameters
#name = GetInput("Navn: ", str)
#costumer = GetInput('Kunde: ', str)
'''
