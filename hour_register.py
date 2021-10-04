import datetime

from lib.get_input import GetInput
from lib import write_files as wf


def hour_register():
    date = datetime.datetime.now()
    month = str(date.month)
    year = str(date.year)
    dir = '../'+ year +'/csv/'

    data = {'Name': GetInput("Navn: ", str),
            'Hours': GetInput('Antall timer: ', float), 
            'Date': date.strftime("%d.%m.%Y"), 
            'Costumer': GetInput('Kunde: ', str)}

    header = list(data.keys())

    df = wf.makeDataFrame(header)
    df_extended = wf.addRowDataFrame(data, df)
    csv = wf.writeToCSV(df_extended,dir,'hour_register.csv')


def sum_over_month():
    
    
    return 0