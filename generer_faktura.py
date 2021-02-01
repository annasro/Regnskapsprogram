import datetime
import os
import pandas

from lib.get_info import *

from lib.layout_invoice import *
from lib.get_input import GetInput

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
deliverydate = invoicedate
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)


#invoice recipient
comp_name, comp_adress, comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno = CompanyInfo(filename)

#invoice sender
costumer_no  = 1
costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone, costumer_no = CostumerInfo(filename,costumer_no)
print(costumer_no)
#create invoice
CreateInvoice(filename,
               comp_name, comp_adress,comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno,
               costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone, costumer_no,
               invoice_no,
               invoicedate,deliverydate,duedate_str,
               year, month)
