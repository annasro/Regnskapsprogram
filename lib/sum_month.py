from .lib1 import*
from .write_files import saveToExcel


def sum_hours_over_month(df, path, path_excel):
    df_new = df
    
    df_new['Date']  = pd.to_datetime(df['Date'], format = '%Y-%m-%d')
   
    
    df_new['month'] = df['Date'].dt.strftime('%m')
    df_new['year']  = df['Date'].dt.strftime('%Y')
    
    
    #df_new.groupby(['date', 'Hours'], as_index=False)['Hours'].sum()
    df_sum = df_new.groupby(['year', 'month'])['Hours'].sum()
    df_sum.columns = ['year', 'month', 'sum']
    print(df_sum)
    
    
    #save to csv
    sheetname = 'sum måneder'
    path = path + 'sum_month.csv'
    
    df_sum.to_csv(path, index = True)
    
    saveToExcel(df_sum, sheetname, path_excel, index = True)







    
