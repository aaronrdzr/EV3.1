import pandas as pd

datos= pd.read_csv('"C:\Users/9aaron\Documents\Tarea\EV3.1.xlsx"', header= None )
print(datos.head())

datos.to_excel('""C:\Users/aaron\Documents\Tarea\EV3.1.xlsx""', sheet_name= 'page', engine='openpyxl'   )
1
