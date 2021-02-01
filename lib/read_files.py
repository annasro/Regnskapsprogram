import pandas as pd

def ReadFiles(path):
    d = pd.read_excel(open(path,vr),sheet_name = sheetname).astype(str)
    df = pd.DataFrame(data = d)
    for i in df:
        dict["key%s" %i] = d.
