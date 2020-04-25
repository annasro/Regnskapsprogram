import pandas as pd
import datetime

def monthly_hours_register(i,data,filename_excel_faktura,month,
                           dtype={'Beskrivelse': str,
                                  'Antall': float, 'Sum': float,
                                  'Timepris': float, 'Bonus': float,
                                  'Netto': float,'Momssats': float,
                                  'Momspris': float,}):
    description = data.Beskrivelse[i]
    quantity = data.Antall[i]
    hourly_rate = data.Timepris[i]
    bonus = data.Bonus[i]
    net_price =  data.Netto[i]
    VAT_rate =  data.Momssats[i]
    VAT_price =  data.Momspris[i]
    sum = data.Sum[i]
    total = data.Totalt[0]
    return description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total

#https://cmdlinetips.com/2018/12/how-to-loop-through-pandas-rows-or-how-to-iterate-over-pandas-rows/
