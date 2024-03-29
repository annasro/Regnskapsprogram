from lib.lib1 import*

from lib.get_input import AskQuestion
from lib.registrer import registrer
from lib.sum_month import sum_hours_over_month

date = datetime.datetime.today()
year = str(date.year)

path  = "G:\Min disk\Enkeltpersonsforetak\Regnskap\\"+year+"\excel\\"
filename = 'stray_' + year

path_excel = path + filename
sheetname = 'timer'
filename = 'timer_' + filename


name = AskQuestion('Navnet på eleven: ', str)
hours = AskQuestion('Hvor hvor mange timer underviste du? ', float)
reisevei = AskQuestion('Hvor lang reisevei i min: ', float)/60

costumer = AskQuestion('Hva er kundenummeret? ', int)

d = datetime.datetime.now()
date = d.strftime("%Y.%m.%d")

data =  {'Name':[name], 'Hours':[hours], 'Reisevei':[reisevei] , 'Date':[date], 'Kundenummer': [costumer]}
registrer(path, filename, path_excel, data, sheetname)

#df_sum = pd.read_csv(path + filename + '.csv')

#sum_hours_over_month(df_sum, path, path_excel)

