import datetime
import os

from lib.get_info import *
from lib.layout_invoice import *



date = datetime.datetime.now()
month = str(date.month)
year = str(date.year)

dir = './excel/'
dir_invoice = './invoice/'
filename = 'test.xlsx'



#filename_accounting ='regnskap'+year+'.xlsx'
#dir_invoice =  '../'+ str(year)+'/Faktura/'

#testdir


#information needed in invoice
invoice_no =  len(os.listdir(dir_invoice)) + 1

#dates
invoicedate =  str(date.day) + "." + str(date.month) + "." + str(date.year)
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)

#invoice recipient
b_name, b_adress, b_postcode, b_mail, b_phone, b_orgno, b_accountno = bedrift_info(filename_excel)

#invoice sender
k_name,k_adress,k_postcode, k_mail = kunde_info(filename_excel,k_nummer)


#create invoice
create_invoice(filename_excel_regnskap,
               b_name, b_adress,b_postcode, b_mail, b_phone, b_orgno, b_accountno,
               k_name,k_adress,k_postcode, k_mail,k_nummer,
               invoice_no,
               invoicedate,deliverydate,duedate_str,
               year, month)
