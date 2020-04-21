'Adding styles to StyleSheet1'
from reportlab.lib.styles import StyleSheet1, ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors


def StyleSheet():
    """Returns a stylesheet object"""
    stylesheet = getSampleStyleSheet()

    stylesheet.add(ParagraphStyle(name='anna',
                                  fontName='Helvetica',
                                  fontSize=10,
                                  leading=6,
                                  spaceBefore=6)
                   )
    stylesheet.add(ParagraphStyle(name='Normal_bold',
                                  fontName='Helvetica-Bold',
                                  fontSize=10,
                                  leading=40,
                                  spaceBefore=6)
                   )

    stylesheet.add(ParagraphStyle(name='Number',
                                  fontName='Times-Roman',
                                  fontSize = 10)
                   )

    stylesheet.add(ParagraphStyle(name='Big',
                                  fontName='Arial',
                                  leftIndent=15,
                                  firstLineIndent=0,
                                  spaceBefore=1,
                                  spaceAfter=7),
                    alias='B')

    
    return stylesheet
