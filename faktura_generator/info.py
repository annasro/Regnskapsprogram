import pandas as pd

def bedrift_info(filename_csv,filename_excel):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Bedrift' ).astype(str)
    b_navn = data.Navn[0]
    b_adresse = data.Adresse[0]
    b_postnummer = data.Postnummer[0]
    b_epost = data.Epost[0]
    b_telefon =  data.Telefon[0]
    b_organisasjonsnummer =  data.Organisajonsnummer[0]
    b_kontonummer =  data.Kontonummer[0]
    data.to_csv(r'./data/csv/'+filename_csv, header = True)
    return b_navn, b_adresse, b_postnummer, b_epost, b_telefon, b_organisasjonsnummer, b_kontonummer

def elev_info(filename_csv,filename_excel,elevnummer):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Elever' ).astype(str)
    e_navn = data.Navn[elevnummer-1]
    e_epost = data.Epost[elevnummer-1]
    e_telefon = data.Telefon[elevnummer-1]
    data.to_csv(r'./data/csv/'+filename_csv, header = True)
    return e_navn, e_epost, e_telefon

def kunde_info(filename_csv,filename_excel,kundenummer):
    data = pd.read_excel(r'./data/excel/'+filename_excel, sheet_name = 'Kunder' ).astype(str)
    k_navn = data.Navn[kundenummer-1]
    k_adresse = data.Adresse[kundenummer-1]
    k_postnummer = data.Postnummer[kundenummer-1]
    k_epost = data.Epost[kundenummer-1]
    data.to_csv(r'./data/csv/'+filename_csv, header = True)
    return k_navn,k_adresse,k_postnummer, k_epost
