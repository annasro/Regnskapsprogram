from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
styles = getSampleStyleSheet()
yourStyle = ParagraphStyle('yourtitle',
                           fontName="Helvetica-Bold",
                           fontSize=16,
                           parent=styles['Heading2'],
                           alignment=1,
                           spaceAfter=14)


Story.append(Paragraph("Whatever printed with yourStyle", yourStyle))
