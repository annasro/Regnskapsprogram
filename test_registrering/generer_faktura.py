import datetime
import os

from lib.get_info import *
from lib.layout_invoice import *

date = datetime.datetime.now()
month = str(date.month)
year = str(date.year)


dir_invoice = './invoice/'
filename = './excel/test.xlsx'

#filename_accounting ='regnskap'+year+'.xlsx'
#dir_invoice =  '../'+ str(year)+'/Faktura/'

#information needed in invoice
invoice_no =  len(os.listdir(dir_invoice)) + 1

#dates
invoicedate =  str(date.day) + "." + str(date.month) + "." + str(date.year)
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)
costumer_no = 1
#invoice recipient
comp_name, comp_adress, comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno = company_info(filename)

#invoice sender
costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone = costumer_info(filename,costumer_no)

'''
#create invoice
create_invoice(filename_excel_regnskap,
               comp_name, comp_adress,comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno,
               costumer_name,costumer_adress,costumer_postcode, costumer_mail,costumer_nummer,
               invoice_no,
               invoicedate,deliverydate,duedate_str,
               year, month)
'''
