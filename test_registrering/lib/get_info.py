import pandas as pd

def company_info(filename):
    data = pd.read_excel(filename, sheet_name = 'Company' ).astype(str)
    comp_name = data.Name[0]
    comp_adress = data.Adress[0]
    comp_postcode = data.Postalcode[0]
    comp_mail = data.Mail[0]
    comp_phone =  data.Phone[0]
    comp_orgno =  data.Orgno[0]
    comp_accountno =  data.Account_number[0]
    return comp_name, comp_adress, comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno


def costumer_info(filename,costumer_no):
    data = pd.read_excel(filename, sheet_name = 'Costumers' ).astype(str)
    costumer_name = data.Name[costumer_no-1]
    costumer_adress = data.Adress[costumer_no-1]
    costumer_postcode = data.Postalcode[costumer_no-1]
    costumer_mail = data.Mail[costumer_no-1]
    costumer_phone = data.Phone[costumer_no-1]
    costumer_no = costumer_no
    return costumer_name,costumer_adress,costumer_postcode, costumer_mail, costumer_phone, costumer_no


def student_info(filename,student_no):
    data = pd.read_excel(r'./data/excel/'+filename, sheet_name = 'Students' ).astype(str)
    student_name = data.Name[student_no-1]
    student_mail = data.Mail[student_no-1]
    student_phone = data.Phone[student_no-1]
    return student_name, student_mail, student_phone
