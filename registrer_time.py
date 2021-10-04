from lib.lib1 import*

from lib.get_input import AskQuestion
from lib.registrer import registrer

path  = './testfolder/'
filename = 'testfile'

path_excel = path + 'testfile'
sheetname = 'timer'

filename = 'timer_' + filename


hours = AskQuestion('Hvor hvor mange timer underviste du? ', str)

name = 'Anna'
costumer = 1
date = 210797

d = datetime.datetime.now()
#date = d.strftime("%Y.%m.%d")

data =  {'Name':[name], 'Hours':[hours], 'Date':[date], 'Kundenummer': [costumer]}
registrer(path, filename, path_excel, data, sheetname)


#sum_hours_over_month()

'''
#input parameters
#name = GetInput("Navn: ", str)
#costumer = GetInput('Kunde: ', str)
'''
