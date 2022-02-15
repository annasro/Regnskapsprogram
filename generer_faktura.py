import datetime
import locale
import os

from lib.get_info import *
from lib.invoice_input import *
from lib.get_input import GetInput

loc = locale.getlocale()
locale.setlocale(locale.LC_ALL, 'nb_NO')

date = datetime.datetime.today()

day = str(date.day)
month = str(date.month)
year = str(date.year)

first = date.replace(day=1)
lastMonth = first - datetime.timedelta(days=1)


lastYear =  (lastMonth.strftime("%Y"))
lastMonth = (lastMonth.strftime("%m"))

datetime_object = datetime.datetime.strptime(lastMonth, "%m")
month_name = datetime_object.strftime("%B")

dir_invoice = '../'+ year + '/invoice/'
print(dir_invoice)

filename = '../'+ year +'/excel/stray_' + year + '.xlsx'


#filename_accounting ='regnskap'+year+'.xlsx'
#dir_invoice =  '../'+ str(year)+'/Faktura/'

#information needed in invoice
invoice_no =  len(os.listdir(dir_invoice))+ 1

#dates
invoicedate =  str(date.day) + "." + str(date.month) + "." + str(date.year)
deliverydate = invoicedate
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)


#invoice recipient
comp_name, comp_adress, comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno = CompanyInfo(filename)

#invoice sender
costumer_no  = GetInput('Kundenummer.: ', int)

costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone, costumer_no = CostumerInfo(filename,costumer_no)

#create invoice
CreateInvoice(filename,
               comp_name, comp_adress,comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno,
               costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone, costumer_no,
               invoice_no,
               invoicedate,deliverydate,duedate_str,
               lastYear, lastMonth,
               year, month, month_name)
