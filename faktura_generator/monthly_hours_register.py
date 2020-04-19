import pandas as pd
import datetime

filename_csv_k = 'data_kunder.csv'
filename_excel = 'info.xlsx'
date = datetime.datetime.now()
month = date.month

def monthly_hours_register(i,data,filename_excel_faktura,month,
                           dtype={'Elevnummer':float,'Beskrivelse': str,
                                  'Antall': float, 'Sum': float,
                                  'Timepris': float, 'Bonus': float,
                                  'Netto': float,'Momssats': float,
                                  'Momspris': float,}):
    studentnumber = data.Elevnummer[i]
    description = data.Beskrivelse[i]
    quantity = data.Antall[i]
    hourly_rate = data.Timepris[i]
    bonus = data.Bonus[i]
    net_price =  data.Netto[i]
    VAT_rate =  data.Momssats[i]
    VAT_price =  data.Momspris[i]
    sum = data.Sum[i]
    date_class = data.Dato[i]
    time = data.Tidspunkt[i]
    total = data.Totalt[0]
    #data.to_csv(r'./data/csv/'+filename_csv, header = True)
    return description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total

#https://cmdlinetips.com/2018/12/how-to-loop-through-pandas-rows-or-how-to-iterate-over-pandas-rows/
