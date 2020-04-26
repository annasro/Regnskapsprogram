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
from layout import *
from monthly_hours_register import*
import sys

#datoer
date = datetime.datetime.now()
invoicedate =  str(date.day) + "." + str(date.month) + "." + str(date.year)
deliverydate = invoicedate
duedate = date + datetime.timedelta(days=14)
duedate_str  = str(duedate.day) + "." + str(duedate.month) + "." + str(duedate.year)
month = str(date.month)
year = str(date.year)

#filenames for excel files
filename_excel = 'info.xlsx'
filename_excel_regnskap = 'regnskap'+year+'.xlsx'

#test if file or dir exist
if not os.path.exists(os.path.join('../', year)):
    open('../'+year, 'w+').close()
if not os.path.exists(os.path.join('../', year, filename_excel_regnskap)):
    open('../'+year+'/'+filename_excel_regnskap, 'w+').close()

e_nummer = 1
k_nummer = 1

list = os.listdir(os.path.join('.../Regnskap/', year,'/Faktura/'))
invoice_no = len(list) + 1

b_name, b_adress, b_postcode, b_mail, b_phone, b_orgno, b_accountno = bedrift_info(filename_excel)
k_name,k_adress,k_postcode, k_mail = kunde_info(filename_excel,k_nummer)
#e_name, e_mail, e_phone = elev_info(filename_excel,e_nummer)


create_invoice(filename_excel_regnskap,
               b_name, b_adress,b_postcode, b_mail, b_phone, b_orgno, b_accountno,
               k_name,k_adress,k_postcode, k_mail,k_nummer,
               invoice_no,
               invoicedate,deliverydate,duedate_str,
               year)
