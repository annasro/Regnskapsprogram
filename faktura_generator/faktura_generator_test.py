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
import sys


'''
if len(sys.argv) == 1:
    print('Skriv inn et filnavn')
    filename = raw_input("Skriv inn filnavn")
else:
    filename = sys.argv[1].csv
    e_ummer = sys.argv[2]
    k_nummer = sys.argv[3]
'''
e_nummer = 1
k_nummer = 1
list = os.listdir('./faktura/') # dir is your directory path
fakturanummer = len(list) + 1

filename_csv_b = 'data_egenpersonsforetak.csv'
filename_csv_e = 'data_elever.csv'
filename_csv_k = 'data_kunder.csv'
filename_excel = 'info.xlsx'

b_navn, b_adresse, b_postnummer, b_epost, b_telefon, b_organisasjonsnummer, b_kontonummer = bedrift_info(filename_csv_b, filename_excel)
k_navn,k_adresse,k_postnummer, k_epost = kunde_info(filename_csv_k, filename_excel,k_nummer)
#e_navn, e_epost, e_telefon = elev_info(filename_csv_e, filename_excel,elevnummer)

#datoer
dato = datetime.datetime.now()
fakturadato =  str(dato.day) + "." + str(dato.month) + "." + str(dato.year)
leveringsdato = fakturadato
dato_forfall = dato + datetime.timedelta(days=14)
forfallsdato  = str(dato_forfall.day) + "." + str(dato_forfall.month) + "." + str(dato_forfall.year)

create_invoice(b_navn, b_adresse, b_postnummer, b_epost, b_telefon, b_organisasjonsnummer, b_kontonummer,k_navn,k_adresse,k_postnummer, k_epost,fakturanummer)
