import pandas as pd

datos= pd.read_csv('C:/Users/aaron/Documents/EV3.1', header= None )
print(datos.head())

datos.to_excel('C:/Users/aaron/Documents/EV3.1', sheet_name= 'page', engine='openpyxl'   )
