from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import StyleSheet1, ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import A4
from monthly_hours_register import*


def create_invoice(filename_excel_regnskap,b_name, b_adress,b_postcode, b_mail, b_phone, b_orgno, b_accountno,
                   k_name,k_adress,k_postcode, k_mail,k_nummer,
                   invoice_no,
                   invoicedate,deliverydate,duedate_str,
                   year,month):

    month = str(int(month) - 1)
    #lage pdf
    c = canvas.Canvas('../'+year+'/Faktura/faktura_' + str(invoice_no)+"_"+ str(invoicedate) + '.pdf')
    data = pd.read_excel(r'../'+year+'/'+filename_excel_regnskap, sheet_name = str(month),decimal=",").astype(str)

    no_data = data.shape[0]

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
    orgno_width =stringWidth(str(b_orgno),fontH ,10)
    h = width - 3.5*margin - orgno_width
    h1 = width - 2*margin
    h2 = width - margin
    midt = width/2.0
    y =  height - margin

    #bedrift
    c.setFont(fontHB, 10)
    c.drawString(v,y, str(b_name))
    c.setFont(fontH, 10)
    c.drawString(h ,y,'Org.nr NO '+ str(b_orgno))
    y -= margin*0.4
    c.drawString(v,y, str(b_adress))
    y -= margin*0.4
    c.drawString(v,y, str(b_postcode))
    y -= margin*0.4
    #Faktura
    c.setFont(fontA, 15)
    c.drawString(h, y, 'Faktura')
    y -= margin
    font1 = fontH
    c.setFont(font1, 10)
    c.drawString(h,y,'Kundenr.: ')
    c.drawString(h1,y, str(k_nummer))
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
    c.drawString(v,y, str(k_name))
    y -= margin*.35
    c.setFont(fontH, 10)
    c.drawString(v,y, str(k_adress))
    y -= margin*.35
    c.drawString(v,y, str(k_postcode))
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


    for i in range(0,no_data):
        description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total, rounding = monthly_hours_register(i,data,filename_excel_regnskap,month)
        c.setFont(fontH, 10)
        c.drawString(v,y, str(description))
        c.drawString(v1,y,str(quantity))
        c.drawString(v2,y,str(hourly_rate))
        c.drawString(v3,y,str(bonus))

        c.drawString(h,y,  str(VAT_rate))
        c.drawString(h1,y, str(net_price))
        y -= margin*.5


    c.drawString(v,y,'Kroneavrunding')
    c.drawString(h1,y,str(rounding))
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
    c.drawString(h,y,'Total:')
    c.setFont(fontTR, 10)
    c.drawString(h1,y,str(total)+',00')
    y -= margin

    c.setFont(fontH, 10)
    #c.drawString(v,y, 'Kommentar: ' + str(kommentar))


    #nederste del av faktura
    y = height - 630
    c.setFont(fontTR, 10)
    c.drawString(midt,y, str(total)+',00')
    y -= margin*0.4
    c.setFont(fontHB, 10)
    c.drawString(h1,y, str(duedate_str))
    c.setFont(fontH, 10)
    c.drawString(v,y,'Kundenr.: ')
    c.drawString(v1-50,y, str(k_nummer))
    y -= margin*0.4
    c.drawString(v,y,'Fakturanr.: ')
    c.drawString(v1-50,y, str(invoice_no))
    y -= margin

    c.drawString(v,y, str(b_name))
    c.drawString(h,y, str(k_name))
    y -= margin*.4
    c.drawString(v,y, str(b_adress))
    c.drawString(h,y, str(k_adress))
    y -= margin*.4
    c.drawString(v,y, str(b_postcode))
    c.drawString(h,y, str(k_postcode))
    y -= margin

    c.setFont(fontTR, 10)
    c.drawString(midt,y,str(total)+',00')
    c.setFont(fontHB, 10)
    c.drawString(h,y,'Kontonummer: ' + str(b_accountno))
    c.setFont(fontH, 10)
    y -= margin*1.3
    c.drawCentredString(midt ,y, b_name + '  |  Org.nr NO ' + b_orgno + '  |  ' + b_mail + '  |  Tlf. ' + b_phone)
    c.save()
