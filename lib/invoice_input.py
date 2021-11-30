from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import StyleSheet1, ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
import pandas as pd


def InvoiceInput(i,df,filename,month,
                           dtype={'Description': str,
                                  'Quantity': float, 'Sum': float,
                                  'Hourly_rate': float, 'Bonus': float,
                                  'Netto': float,'MVA': float,
                                  'MVA_cost': float,}):
    description = df.Description[i]
    quantity = df.Quantity[i]
    hourly_rate = df.Hourly_rate[i]
    bonus = df.Bonus[i]
    net_price =  df.Netto[i]
    VAT_rate =  df.MVA[i]
    VAT_price =  df.MVA_cost[i]
    sum = df.Sum[i]
    total = float(df.Total[0])

    return description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total


def CreateInvoice(filename,
                   comp_name, comp_adress,comp_postcode, comp_mail, comp_phone, comp_orgno, comp_accountno,
                   costumer_name, costumer_adress, costumer_postcode, costumer_mail, costumer_phone, costumer_no,
                   invoice_no,
                   invoicedate, deliverydate, duedate_str,
                   year, month):
    month = str(int(month)-1)
    #lage pdf
    #c = canvas.Canvas('../'+year+'/Faktura/faktura_' + str(invoice_no)+"_"+ str(invoicedate) + '.pdf')
    #df = pd.read_excel(r'../'+year+'/'+filename, sheet_name = str(month),decimal=",").astype(str)
    c = canvas.Canvas('../'+year+'/invoice/faktura_' + str(invoice_no)+"_"+ str(invoicedate) + '.pdf')
    df = pd.read_excel(r'./'+filename, sheet_name = str(month)).astype(str)

    no_df = df.shape[0]

    #sidestørrelse
    c.setPageSize(A4)
    c.setTitle(str(invoice_no))
    width, height = A4
    margin = 40

    #logo
    #c.drawInlineImage('logo.jpg', start_x, start_y, width = bilde_bredde, height = bilde_høyde)

    pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))
    c.getAvailableFonts()
    fontH = 'Helvetica'
    fontHB = 'Helvetica-Bold'
    fontA = 'Arial'
    fontTR = 'Times-Roman'

    #elementposisjoner
    v =  margin
    v1 = v +  margin*3
    v2 = v1 + margin*2
    v3 = v2 + margin*2
    v4 = v3 + margin*2
    orgno_width =stringWidth(str(comp_orgno),fontH ,10)
    h = width - 3.5*margin - orgno_width
    h1 = width - 2*margin
    h2 = width - margin
    midt = width/2.0
    y =  height - margin

    #bedrift
    c.setFont(fontHB, 10)
    c.drawString(v,y, str(comp_name))
    c.setFont(fontH, 10)
    c.drawString(h ,y,'Org.nr NO '+ str(comp_orgno))
    y -= margin*0.4
    c.drawString(v,y, str(comp_adress))
    y -= margin*0.4
    c.drawString(v,y, str(comp_postcode))
    y -= margin*0.4
    #Faktura
    c.setFont(fontA, 15)
    c.drawString(h, y, 'Faktura')
    y -= margin
    font1 = fontH
    c.setFont(font1, 10)
    c.drawString(h,y,'Kundenr.: ')
    c.drawString(h1,y, str(costumer_no))
    y -= margin*.35
    c.drawString(h,y,'Fakturanr.: ')
    c.drawString(h1,y, str(invoice_no))
    y -= margin*.35

    #fakurainfo
    c.drawString(h,y,'Fakturadato: ')
    c.drawString(h1,y, str(invoicedate))
    y -= margin*.35
    c.drawString(h,y,'Forfallsdato:')
    c.setFont(fontHB, 10)
    c.drawString(h1,y, str(duedate_str))
    y -= margin*.35
    c.setFont(fontH, 10)
    c.drawString(h,y,'Leveringsdato: ')
    c.drawString(h1,y, str(deliverydate))
    y -= margin

    #kunde
    c.setFont(fontHB, 10)
    c.drawString(v,y, str(costumer_name))
    y -= margin*.35
    c.setFont(fontH, 10)
    c.drawString(v,y, str(costumer_adress))
    y -= margin*.35
    c.drawString(v,y, str(costumer_postcode))
    y -= margin*2
    y = height -350


    #midtdel
    c.drawString(v,y,   'Beskrivelse:')
    c.drawString(v1,y,  'Antall:')
    c.drawString(v2,y,  'Pris:' )
    c.drawString(v3,y,  'Bonus:' )
    c.drawString(h,y,   'MVA sats i %:' )
    c.drawString(h1,y,  'Netto pris:')
    y -= margin*.1

    c.setStrokeColorRGB(1/120.0,1/120.0,1/120.0)
    c.line(margin,y,width-margin,y)
    y -= margin*.4


    for i in range(0,no_df):
        description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total = InvoiceInput(i,df,filename,month)
        c.setFont(fontH, 10)
        import locale
        import datetime
        
        loc = locale.getlocale()
        locale.setlocale(locale.LC_ALL, 'nb_NO')
        date = datetime.datetime.now()
        month = date.month 
    
        month = datetime.date(1900,month - 1,1).strftime('%B')

        c.drawString(v,y, str(description + ' ' + str(month)))
        c.drawString(v1,y,str(quantity))
        c.drawString(v2,y,str(hourly_rate))
        c.drawString(v3,y,str(bonus))

        c.drawString(h,y,  str(VAT_rate))
        net_price = float(net_price)
        c.drawString(h1,y, "%.2f" %net_price)
        y -= margin*.5


    y -= margin*.8

    c.setFont('Helvetica-Oblique',10)
    textWidth = stringWidth('Alle beløp er oppgitt i NOK', 'Helvetica-Oblique', 10)
    c.drawString(width-margin-textWidth,y, 'Alle beløp er oppgitt i NOK')
    y -= margin *2
    c.setFont(fontHB, 10)
    c.drawString(h,y,'MVA:')
    c.setFont(fontTR, 10)
    c.drawString(h1,y, str(VAT_price)+',00')
    y -= margin*.4
    c.setFont(fontHB, 10)
    c.drawString(h,y,'Totalt:')
    c.setFont(fontTR, 10)
    c.drawString(h1,y,'%0.2f'%total)
    y -= margin

    c.setFont(fontH, 10)
    #c.drawString(v,y, 'Kommentar: ' + str(kommentar))


    #nederste del av faktura
    y = height - 630
    c.setFont(fontTR, 10)
    c.drawString(midt,y, '%0.2f'%total)
    y -= margin*0.4
    c.setFont(fontHB, 10)
    c.drawString(h1,y, str(duedate_str))
    c.setFont(fontH, 10)
    c.drawString(v,y,'Kundenr.: ')
    c.drawString(v1-50,y, str(costumer_no))
    y -= margin*0.4
    c.drawString(v,y,'Fakturanr.:')
    c.drawString(v1-50,y, '00'+str(invoice_no))
    y -= margin

    c.drawString(v,y, str(comp_name))
    c.drawString(h,y, str(costumer_name))
    y -= margin*.4
    c.drawString(v,y, str(comp_adress))
    c.drawString(h,y, str(costumer_adress))
    y -= margin*.4
    c.drawString(v,y, str(comp_postcode))
    c.drawString(h,y, str(costumer_postcode))
    y -= margin

    c.setFont(fontTR, 10)
    c.drawString(midt,y,'%0.2f'%total)
    c.setFont(fontHB, 10)
    c.drawString(h,y,'Kontonummer: ' + str(comp_accountno))
    c.setFont(fontH, 10)
    y -= margin*1.3
    c.drawCentredString(midt ,y, comp_name + '  |  Org.nr NO ' + comp_orgno + '  |  ' + comp_mail + '  |  Tlf. ' + comp_phone)
    c.save()
