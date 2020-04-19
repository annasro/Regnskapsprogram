from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from monthly_hours_register import*
#funksjon som lager regningen

def create_invoice(filename_excel_faktura,data,no_data,b_name, b_adress,b_postcode, b_mail, b_phone, b_orgno, b_accountno,
                   k_name,k_adress,k_postcode, k_mail,k_nummer,
                   invoice_no,
                   invoicedate,deliverydate,duedate_str):

    #lage pdf
    c = canvas.Canvas('./faktura/'+'faktura_' + str(invoice_no)+"_"+ str(invoicedate) + '.pdf')
    #sidestørrelse
    c.setPageSize(A4)

    #logo
    #c.drawInlineImage('logo.jpg', start_x, start_y, width = bilde_bredde, height = bilde_høyde)

    #sidestørrelse A4
    width, height = A4
    margin = 40
    pdfmetrics.registerFont(TTFont('Arial','Arial.ttf'))

    #elementposisjoner
    v =  margin
    v1 = v +  margin*3
    v2 = v1 + margin*2
    v3 = v2 + margin*2
    v4 = v3 + margin*2
    orgno_width =stringWidth(str(b_orgno),'Helvetica',10)
    h = width - 3.5*margin - orgno_width
    h1 = width - 2*margin
    midt = width/2.0
    y =  height - margin

    #bedrift
    c.setFont('Helvetica-Bold', 10)
    c.drawString(v,y, str(b_name))
    c.setFont('Helvetica', 10)

    c.drawString(h ,y,'Org.nr NO'+ str(b_orgno))
    y -= margin*0.4
    c.drawString(v,y, str(b_adress))
    y -= margin*0.4
    c.drawString(v,y, str(b_postcode))
    y -= margin*0.4
    #Faktura
    c.setFont('Arial', 15)
    c.drawString(h, y, 'Faktura')
    y -= margin

    c.setFont('Helvetica', 10)
    c.drawString(v,y, str(b_mail))
    c.drawString(h,y,'Kundenr.: ')
    c.drawString(h1,y, str(k_nummer))
    y -= margin*.45
    c.drawString(v,y, 'Telefon: '+ str(b_phone))
    c.drawString(h,y,'Fakturanr.: ')
    c.drawString(h1,y, str(invoice_no))
    y -= margin*.4


    #fakurainfo
    c.drawString(h,y,'Fakturadato: ')
    c.drawString(h1,y, str(invoicedate))
    y -= margin*.4
    c.drawString(h,y,'Forfallsdato:')
    c.setFont('Helvetica-Bold', 10)
    c.drawString(h1,y, str(duedate_str))
    y -= margin*.4
    c.setFont('Helvetica', 10)
    c.drawString(h,y,'Leveringsdato: ')
    c.drawString(h1,y, str(deliverydate))
    y -= margin

    #kunde
    c.setFont('Helvetica-Bold', 10)
    c.drawString(v,y, str(k_name))
    y -= margin*.4
    c.setFont('Helvetica', 10)
    c.drawString(v,y, str(k_adress))
    y -= margin*.4
    c.drawString(v,y, str(k_postcode))
    y -= margin*2
    y = height -350


    #midtdel
    c.drawString(v,y,   'Beskrivelse')
    c.drawString(v1,y,  'Antall')
    c.drawString(v2,y,  'Timepris' )
    c.drawString(v3,y,  'Bonus' )
    c.drawString(h,y,   'MVA sats:' )
    c.drawString(h1,y,  'Netto pris')
    y -= margin*.4



    for i in range(0,no_data):
        description, quantity, hourly_rate, bonus, net_price, VAT_rate, VAT_price, sum,total = monthly_hours_register(i,data,filename_excel_faktura,month)
        c.setFont('Helvetica', 10)
        c.drawString(v,y, str(description))
        c.drawString(v1,y,str(quantity))
        c.drawString(v2,y,str(hourly_rate))
        c.drawString(v3,y,str(bonus))

        c.setFont('Times-Roman', 10)
        c.drawString(h,y,  '0.00 %')
        c.drawString(h1,y, str(net_price))
        y -= margin*.4

    y -= margin *2
    c.setFont('Helvetica-Bold', 10)
    c.drawString(h,y,'MVA:')
    c.setFont('Times-Roman', 10)
    c.drawString(h1,y, str(VAT_price))
    y -= margin*.4
    c.setFont('Helvetica-Bold', 10)
    c.drawString(h,y,'Total:')
    c.setFont('Times-Roman', 10)
    c.drawString(h1,y,str(total))
    y -= margin

    c.setFont('Helvetica', 10)
    #c.drawString(v,y, 'Kommentar: ' + str(kommentar))


    #nederste del av faktura
    y = height - 630
    c.setFont('Times-Roman', 10)
    c.drawString(midt,y, str(total))
    y -= margin*0.4
    c.setFont('Helvetica-Bold', 10)
    c.drawString(h1,y, str(duedate_str))
    c.setFont('Helvetica', 10)
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

    c.setFont('Times-Roman', 10)
    c.drawString(midt,y,str(total))
    c.setFont('Helvetica', 10)
    c.drawString(h,y,'Kontonummer: ' + str(b_accountno))
    c.setFont('Helvetica-Bold', 10)
    c.drawStringCenterd('Anna Stray Rongve | Org.nr NO ' + b_orgno + ' | ' + b_mail + 'Tlf.' + b_phone)
    c.save()
