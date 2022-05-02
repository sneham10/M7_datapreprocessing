import pandas as pd
df=pd.read_csv('sales.csv')
#printing info
print(df.info())
#fix the formate like date
df['Order Date']=pd.to_datetime(df['Order Date'])
#fix the formate like date
df['Ship Date']=pd.to_datetime(df['Ship Date'])
#checking presence of duplicate
print(df.duplicated())
#removing country 
del df['Country']

del df['Unit Price']
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['year'] = df['Order Date'].dt.year
print(df)
#saving in another file
df.to_csv('cleaned1.csv')


