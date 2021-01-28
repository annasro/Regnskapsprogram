import pandas as pd

def bedrift_info(filename_excel):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Bedrift' ).astype(str)
    b_name = data.Navn[0]
    b_adress = data.Adresse[0]
    b_postcode = data.Postnummer[0]
    b_mail = data.Epost[0]
    b_phone =  data.Telefon[0]
    b_orgno =  data.Organisajonsnummer[0]
    b_accountno =  data.Kontonummer[0]
    return b_name, b_adress, b_postcode, b_mail, b_phone, b_orgno, b_accountno

def elev_info(filename_excel,elevnummer):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Elever' ).astype(str)
    e_name = data.Navn[elevnummer-1]
    e_mail = data.Epost[elevnummer-1]
    e_phone = data.Telefon[elevnummer-1]
    return e_name, e_mail, e_phone

def kunde_info(filename_excel,kundenummer):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Kunder' ).astype(str)
    k_name = data.Navn[kundenummer-1]
    k_adress = data.Adresse[kundenummer-1]
    k_postcode = data.Postnummer[kundenummer-1]
    k_mail = data.Epost[kundenummer-1]
    return k_name,k_adress,k_postcode, k_mail
