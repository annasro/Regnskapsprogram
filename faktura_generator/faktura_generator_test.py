#library to import the excel file
from openpyxl import load_workbook
#libraries to create the pdf file and add text to it
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
#library to get logo related information
from PIL import Image
import datetime
import os
import pandas
from info import *
from create_invoice import *
from monthly_hours_register import*
import sys


'''
if len(sys.argv) == 1:
    print('Skriv inn et filname')
    filename = raw_input("Skriv inn filname")
else:
    filename = sys.argv[1].csv
    e_ummer = sys.argv[2]
    k_nummer = sys.argv[3]
'''

filename_csv_b = 'data_egenpersonsforetak.csv'
filename_csv_e = 'data_elever.csv'
filename_csv_k = 'data_kunder.csv'
filename_excel = 'info.xlsx'
filename_excel_faktura = 'faktura_mal.xlsx'

e_nummer = 1
k_nummer = 1
i = 0

#list = os.listdir('./faktura/test') # dir is your directory path
#invoice_no = len(list) + 1
invoice_no = 0

#datoer
date = datetime.datetime.now()
invoicedate =  str(date.day) + "." + str(date.month) + "." + str(date.year)
deliverydate = invoicedate
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)
month = str(date.month)

b_name, b_adress, b_postcode, b_mail, b_phone, b_orgno, b_accountno = bedrift_info(filename_csv_b, filename_excel)
k_name,k_adress,k_postcode, k_mail = kunde_info(filename_csv_k, filename_excel,k_nummer)
#e_name, e_mail, e_phone = elev_info(filename_csv_e, filename_excel,e_nummer)

#lese fil
data = pd.read_excel(r'./'+ filename_excel_faktura, sheet_name = str(month)).astype(str)
no_data = data.shape[0]

create_invoice(filename_excel_faktura,data,no_data,b_name, b_adress,b_postcode, b_mail, b_phone, b_orgno, b_accountno,
                k_name,k_adress,k_postcode, k_mail,k_nummer,
                invoice_no,
                invoicedate,deliverydate,duedate_str)
