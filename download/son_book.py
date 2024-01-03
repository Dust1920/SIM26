import os
import pandas as pd

# Extraemos el listado de archivos tipo excel. 
sonora_data = os.listdir('raw_data\\Municipios')

# Definimos el constructor del archivo excel.
excelw = pd.ExcelWriter('medium_data\\book_son.xlsx')

for mun in sonora_data:
    muns = mun[4:-5]
    path = 'raw_data\\Municipios\\' + mun
    raw = pd.read_excel(path)
    raw.to_excel(excelw, sheet_name=muns)

excelw.close()