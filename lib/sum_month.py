from lib.lib1 import*


def sum_hours_over_month(df):
    df_new = df
    df_new['Date'] = pd.to_datetime(df['Date'])
    df_new['date_month'] = df['Date'].dt.strftime('%Y-%m')
    
    df.groupby(['date_month', 'Category'], as_index=False)['Amount'].sum()
    
    
