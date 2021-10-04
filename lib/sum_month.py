from .lib1 import*


def sum_hours_over_month(df, path):
    print(df)
    df_new = df
    df_new['Date'] = pd.to_datetime(df['Date'])
    df_new['date_month'] = df['Date'].dt.strftime('%Y-%m')
    sum = df_new.groupby(['date_month', 'Hours'], as_index=False)['Hours'].sum()
    
    #save to csv
    sheetname = 'sum måneder'
    sum.to_csv(path + 'sum_month.csv', index = False)
    
    #sum_df = sum_hours_over_month(pd.read_csv(filename))
    
    #saveToExcel(sum_df, sheetname, path_excel)







    
