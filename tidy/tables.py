"""
Este código es una recopilación de la creación de las columas dentro de tables_tidy.py, en orden alfabetico. 
"""

import pandas as pd
import indicators_tables
import regex as re

Sonora = pd.read_excel('..\\medium_data\\book_son.xlsx',sheet_name=None)
Municipios = list(Sonora.keys())
sonora = {municipio: indicators_tables.indicators_tables(Sonora, municipio) for municipio in Municipios}


mun = Municipios[0]
mi = [] # Almacenamiento de indices.

### Funciones Auxiliares

def footnote(data: pd.DataFrame):
    extra_information = []
    extra_codes = ['Nota','^\d']
    remove_codes = ['Fuente']
    for i in list(data.index):
        for code in extra_codes:
            if re.findall(code, i):
                extra_information.append(i)
                data = data.drop(index = i)
        for code in remove_codes:
            if re.findall(code, i):
                data = data.drop(index = i)
    return data, extra_information


def format_df(df: pd.DataFrame):
    df.columns = df.iloc[0]
    df.drop(index = df.index[0],inplace=True)
    df.set_index(df.columns[0], inplace= True)
    df, extra = footnote(df)
    df = df.replace({"nan" : pd.NA}).dropna(axis = 1, how = "all").iloc[:, :2]
    return df, extra

def dataframe_tolist(data: pd.DataFrame):
    y = []
    for i in list(data.index):
        for j in list(data.columns):
            y.append(data.loc[i,j])
    return y

###  Patterns 
note_pattern = "Nota"
feet_pattern = '^\d'
inegi = 'INEGI'
age_pattern = "\d+\sa\s\d+| 25"
plantel_pattern = "Plantel"
escol_pattern = "Población (con|sin)"

clast = ['Absoluto', 'Porcentaje']

# Accidentes

df = sonora[mun][19].copy()
df, extra_acc = format_df(df)

acc0 = list(df.index)
acc_one = [c for c in acc0 for j in range(2)]
acc_two = [last  for j in range(len(acc0)) for last in clast]

mi_acc = pd.MultiIndex.from_arrays([acc_one, acc_two])
acc2022_df = pd.DataFrame(index = Municipios, columns= mi_acc) 

mi.append(mi_acc)

# Vehículos
df = sonora[mun][18].copy()
df, extra_cars = format_df(df)

c0 = list(df.index)
cars_one = [c for c in c0 for j in range(2)]
cars_two = [last for j in range(len(c0))  for last in clast]

mi_cars = pd.MultiIndex.from_arrays([cars_one, cars_two])
cars2022_df = pd.DataFrame(index = Municipios, columns= mi_cars) 

mi.append(mi_cars)

# Composicion Territorial 

level_two = ['Absoluto','Porcentaje']
level_zero = ['Localidades', 'AGEB', 'Manzanas']
level_one = ['Total','Urbanas','Rurales']

lzero = len(level_zero)
lone = len(level_one)
ltwo = len(level_two)
ltotal = lzero*lone*ltwo

col_two = [two for j in range(lzero * lone)  for two in level_two ]
colone = [[one for one in level_one for j in range(ltwo)] for k in range(lzero)]
for l in range(lzero):
    if l == 0:
        col_one = colone[l]
    else:
        col_one += colone[l]
col_zero = [zero for zero in level_zero for j in range(lone * ltwo)]

mi_compos = pd.MultiIndex.from_arrays([col_zero, col_one, col_two])
compos_df = pd.DataFrame(index = Municipios, columns=mi_compos)
mi.append(mi_compos)  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



# Dinámica Poblacional Check

## Pob
c0 = ['Población Total','Tasa de Crecimiento Poblacional', 'Indice', 'Migración']
c1_pob = ['Año', 'Sexo', 'Edad', 'Localidades']
c1_values = {
    'Año' : ['1990','2000','2010','2020'],
    'Sexo': ['Masculino', 'Fememino'],
    'Edad': ['0-14', '15-64','65+'],
    'Localidades': ['1-2499','+2500']
}
clast = ['Absoluto', 'Porcentaje']

pob_two = [c for cat in c1_pob for c in c1_values[cat] for j in range(len(clast))]
pob_one = [c1 for c1 in c1_pob for j in range(len(c1_values[c1]) * len(clast))]
pob_three = [c for j in range(len(pob_two) // 2) for c in clast ]
pob_zero = [c0[0] for j in range(len(pob_two))]

submi_pob = pd.MultiIndex.from_arrays([pob_zero, pob_one, pob_two, pob_three])
pob_df = pd.DataFrame(index = Municipios, columns=submi_pob)

## TCP
c2_one = ['Periodo']
c2_two = ['1990-2000','2000-2010', '2010-2020']

tcp_two = [c2  for c2 in c2_two for j in range(len(clast))]
tcp_one = [c2 for c2 in c2_one for j in range(len(tcp_two))]
tcp_three = [c for j in range(len(tcp_two) // 2) for c in clast ]
tcp_zero = [c0[1] for j in range(len(tcp_two))]

submi_tcp = pd.MultiIndex.from_arrays([tcp_zero, tcp_one, tcp_two, tcp_three])
df_tcp = pd.DataFrame(index = Municipios, columns=submi_tcp)

## Indice
c1_ind = ['Edad mediana', 'Edad mediana',
          'Razón de dependencia', 'Razón de dependencia',
          'Índice de envejecimiento', 'Índice de envejecimiento', 
          'Promedio de hijas e hijos nacidos vivos por mujer',
            'Promedio de hijas e hijos nacidos vivos por mujer']
c2_ind = ['(1)', '(1)', '(2)', '(2)', '(3)', '(3)', '(4)', '(4)']
c3_ind = ['Absoluto','Porcentaje',
          'Absoluto','Porcentaje',
          'Absoluto','Porcentaje',
          'Absoluto','Porcentaje',]
indice_zero = [c0[2] for i in range(len(c1_ind))]

submi_ind = pd.MultiIndex.from_arrays([indice_zero, c1_ind, c2_ind, c3_ind])
df_ind = pd.DataFrame(index = Municipios, columns = submi_ind)

## Migracion

c1_migra = ['Total', 'Causa']
c2_migra = ['Trabajo', 'Asuntos Familiares', 'Estudio', 'Inseguridad delictiva o Violencia', 'Otro']

migra_three = [three  for j in range(len(c2_migra) + 1) for three in clast]
migra_two_1 = ["",""]
migra_two_2 = [two for two in c2_migra for j in range(len(clast))]
migra_two = migra_two_1 + migra_two_2
migra_one_1 = [one for one in c1_migra for j in range(len(clast))]
migra_one_2 = [c1_migra[1] for j in range(2 * (len(c2_migra) - 1))]
migra_one = migra_one_1 + migra_one_2
migra_zero = [c0[3] for i in range(len(migra_one))]


submi_migra = pd.MultiIndex.from_arrays([migra_zero, migra_one, migra_two, migra_three])
df_migra = pd.DataFrame(index = Municipios, columns= submi_migra)

u = pd.concat([pob_df, df_tcp, df_ind, df_migra], axis = 1)
mi.append(u.columns)

# Economía

df = sonora[mun][21].copy()
df, extra_economy = format_df(df)

cols = list(df.index)

economy = {
"type": ['Por Sector', 'Por Nivel de Ingreso (Salarios Minímos)'],
"level": ["Total"," 1","1-2","2-3","3-5", "+5","No recibe ingresos"],
"sector": ["Total", "Primario", "Minería, industrias manufactureras, electricidad y agua", "Construcción", "Comercio", "Servicios"]
}

c0_1 = cols[:3]
c0_3 = cols[-3:]

econ_three_1 = [last  for j in range(len(c0_1)) for last in clast]
econ_three_3 = econ_three_1
econ_two_1 = [""  for j in range(len(c0_1)) for last in clast]
econ_two_3 = econ_two_1
econ_one_1 = econ_two_1
econ_one_3 = econ_two_1
econ_one_2 = ['Por sector' for j in range(len(economy['sector'] * len(clast)))] + ['Por Nivel de Ingreso (Salarios Minimos)' for j in range(len(economy['level'] * len(clast)))]
econ_two_2 =[sec for sec in economy["sector"] for j in range(len(clast)) ] + [lev for lev in economy['level'] for j in range(len(clast))]
econ_three_2 = [last for j in range(len(econ_one_2) // 2) for last in clast]

econ_zero_1 = [c for c in c0_1 for j in range(len(clast))]
econ_zero_3 = [c for c in c0_3 for j in range(len(clast))]
econ_zero_2 = len(econ_two_2) * ['Poblacion Ocupada de 12 años y más']

econ_zero = econ_zero_1 + econ_zero_2 + econ_zero_3
econ_one = econ_one_1 + econ_one_2 + econ_one_3
econ_two = econ_two_1 + econ_two_2 + econ_two_3
econ_three = econ_three_1 + econ_three_2 + econ_three_3
mi_econ = pd.MultiIndex.from_arrays([econ_zero, econ_one, econ_two, econ_three])
econ_df = pd.DataFrame(index = Municipios, columns=mi_econ)

mi.append(mi_econ)


# Educación

## Intro
edu_intro_c0 = ['Población Analfabeta','Población Analfabeta',
                    'Grado Promedio de Escolaridad', 'Grado Promedio de Escolaridad']
edu_intro_c1 = [last for j in range(len(edu_intro_c0) // 2) for last in clast]
cm1 = ["" for j in range(len(edu_intro_c0))]
cm2 = cm1.copy()
mi_edu_intro = pd.MultiIndex.from_arrays([cm2, cm1, edu_intro_c0, edu_intro_c1])
edu_df_intro = pd.DataFrame(index = Municipios, columns=mi_edu_intro)

## Rest

education = {
    "cat0": ['Educación','Planteles'],
    "cat1": ['Edad','Escolaridad'],
    "cat1": ['Planteles'],
    "age" : ["Total", "3-5","6-11","12-14","15-17","18-24","+25"],
    "plantel" : ["Total", "Educación Inicial","Preescolar","Primaria","Secundaria","Bachillerato"],
    "escol" : ["Total", "Sin Escolaridad","Básica","Media Superior","Superior"]
}

edu_age_c2 = [age for age in education["age"] for j in range(len(clast))]
edu_pl_c2 = [pl for pl in education["plantel"] for j in range(len(clast))]
edu_escol_c2 = [escol for escol in education["escol"] for j in range(len(clast))]

edu_escage_c1 = ['Edad' for j in range(len(edu_age_c2))] + ['Escolaridad' for j in range(len(edu_escol_c2))]
edu_pl_c1 = ['Sector' for j in range(len(edu_pl_c2))]

edu_c1 = edu_escage_c1 + edu_pl_c1
edu_c2 = edu_age_c2 + edu_escol_c2 + edu_pl_c2
edu_c0 = ['Educación' for j in range(len(edu_escage_c1))] + ['Plantel' for j in range(len(edu_pl_c1))]
edu_c3 = [last  for j in range(len(edu_c1) // 2) for last in clast]


mi_edu = pd.MultiIndex.from_arrays([edu_c0,edu_c1,edu_c2,edu_c3])
df_edu = pd.DataFrame(index = Municipios, columns= mi_edu)

df_edu = pd.concat([edu_df_intro, df_edu])
mi.append(df_edu.columns)


# Entorno Urbano
# Entorno Urbano P1

df = sonora[mun][14].copy()
df, extra_urban = format_df(df)
df

c0_1 = df.index[0]
c0_2 = ['Alumbrado Público', 'Recubrimiento', 'Guarnición', 'Rampa para silla de Ruedas']
c1 = ['Todas', 'Alguna', 'Ninguna']

u0 = [c0 for c0 in c0_2 for j in range(len(clast) * len(c1))]
u1 = len(c0_2) * ['Todas', 'Todas', 'Alguna', 'Alguna', 'Ninguna', 'Ninguna']
u2 = [c  for j in range(len(c1) * len(c0_2)) for c in clast]

v0 = [c0_1, c0_1]
v1 = ["",""]
v2 = clast

urban_zero = v0 + u0
urban_one = v1 + u1
urban_two = v2 + u2

mi_urban = pd.MultiIndex.from_arrays([urban_zero, urban_one, urban_two])

urban2020_df = pd.DataFrame(index = Municipios, columns=mi_urban)


## Entorno Urbano P2
c0_2 = ['Letrero con nombre de la calle', 'Banqueta', 'Transporte colectivo']
c1 = ['Todas', 'Alguna', 'Ninguna']

u0 = [c0 for c0 in c0_2 for j in range(len(clast) * len(c1))]
u1 = len(c0_2) * ['Todas', 'Todas', 'Alguna', 'Alguna', 'Ninguna', 'Ninguna']
u2 = [c  for j in range(len(c1) * len(c0_2)) for c in clast]

urban_zero = u0
urban_one =  u1
urban_two = u2

mi_urban_2 = pd.MultiIndex.from_arrays([urban_zero, urban_one, urban_two])
urban2020_2 = pd.DataFrame(index = Municipios, columns=mi_urban_2)



urban_2020 = pd.concat([urban2020_df, urban2020_2], axis = 1)

mi.append(urban_2020.columns)


# Infraestructura 
df1 = sonora[mun][16].copy()
df1, extra_struct = format_df(df1)
df2 = sonora[mun][17].copy()
df2, extra_struct2 = format_df(df2)

df = pd.concat([df1, df2])
struct_df = pd.DataFrame(index = Municipios, columns= df.index)

mi.append(list(df.index))


# Estructura por Sexo

df = sonora[mun][5].copy()
df = df.set_index(df.columns[0])
extra_gender = []


for i in list(df.index):
    if re.findall(note_pattern, i):
        extra_gender.append(i)
        df = df.drop(index = i)
    if re.findall(inegi, i):
        df = df.drop(index = i)
df = df.replace({"nan":pd.NA}).dropna(axis = 1, how = 'all')
df.columns = df.iloc[1]
df = df.drop(index = ["Estructura de la población por edad y sexo, 2020"]).iloc[1:,:3]
df = df.set_index('Edad')


c0 = list(df.index)
c1 = ["%H", "%M"]

genderage_one = [one for j in range(len(c0)) for one in c1 ]
genderage_zero = [zero for zero in c0 for j in range(len(c1))]

mi_genderage = pd.MultiIndex.from_arrays([genderage_zero, genderage_one])
dgenage_df = pd.DataFrame(index = Municipios, columns= mi_genderage)

mi.append(mi_genderage) # 4


# Finanzas Municipales


df = sonora[mun][22].copy()
ingresos2021, extra_fin1 = format_df(df)

df2 = sonora[mun][23].copy()
egresos2021, extra_fin2 = format_df(df2)

c0 = ingresos2021.index
c1 = [last  for j in range(len(c0)) for last in clast]
ingresos_zero = [c for c in c0 for j in range(len(clast))]

mi_ingresos = pd.MultiIndex.from_arrays([ingresos_zero, c1])
ingresos_df = pd.DataFrame(index = Municipios, columns= mi_ingresos)


c00 = egresos2021.index
c01 = [last  for j in range(len(c00)) for last in clast]
egresos_zero = [c for c in c00 for j in range(len(clast))]

mi_egresos = pd.MultiIndex.from_arrays([egresos_zero, c01])
egresos_df = pd.DataFrame(index = Municipios, columns= mi_egresos)

egin = ['Ingresos' for j in range(len(ingresos_df.columns))] + ['Egresos' for j in range(len(egresos_df.columns))]

c0 = ingresos2021.index
c1 = [last  for j in range(len(c0)) for last in clast]
ingresos_zero = [c for c in c0 for j in range(len(clast))]

mi_egin = pd.MultiIndex.from_arrays([egin,ingresos_zero + egresos_zero, c1 + c01]) 

egin = pd.DataFrame(index = Municipios, columns = mi_egin)

mi.append(mi_egin)


# Grupos Vulnerables.
c0_vul = [ "Población","Población","Población",
          "Población","Población", "Población",
          "Población","Población","Población",
          "Población","Población", "Población",
          'Personas', 'Personas', 'Personas', 'Personas',
          'Personas', 'Personas', 'Personas', 'Personas']
    
    
c1_vul = ["Hablante de lengua indígena", "Hablante de lengua indígena", "Hablante de lengua indígena", "Hablante de lengua indígena",
          "Con discapacidad",  "Con discapacidad", "Con alguna limitación en la actividad", 
          "Con alguna limitación en la actividad", "Con algún problema o condición mental",
          "Con algún problema o condición mental", "Sin acta de nacimiento", "Sin acta de nacimiento",
          "Pobreza", "Pobreza", "Pobreza", "Pobreza", "Pobreza", "Pobreza", 
            "Madres menores de 20 años", "Madres menores de 20 años"]

c2_vul = ["De 3 años y más", "De 3 años y más", "De 3 años y más", "De 3 años y más",
          "","","", "", "","","", "", "(1)", "(1)", "(1)", "(1)", "(1)", "(1)", "(2)", "(2)"]

c3_vul = ['Total', 'Total', 'No habla español', 'No habla español',  "",
          "", "", "",  "", "",
          "", "", "Total", "Total", "Extrema",
          "Extrema", "Moderada", "Moderada", "", ""]
c4_vul = [last for j in range(len(c3_vul) // 2) for last in clast ]

mi_vul = pd.MultiIndex.from_arrays([c0_vul,c1_vul,c2_vul,c3_vul,c4_vul])
vul_df = pd.DataFrame(index = Municipios, columns=mi_vul)

mi.append(mi_vul)

# Hechos Vitales

vitals_c0 = ['Nacimientos', 'Nacimientos',
              'Defunciones', 'Defunciones', 'Defunciones', 'Defunciones', 'Defunciones',
              'Defunciones', 'Defunciones', 'Defunciones', 'Defunciones', 'Defunciones',
              'Matrimonios', 'Matrimonios', 'Divorcios', 'Divorcios']
vitals_c1 = ["", "", "Total","Total", "Causa","Causa", "Causa", "Causa","Causa", "Causa", 
             "Fetales", "Fetales",
             "","", "",""]
vitals_c2 = ["","", "","", "Accidente", "Accidente", "Homicidio", "Homicidio",
            "Suicidio", "Suicidio","",
             "","", "","", ""]
vitals_c3 = [three for j in range(len(vitals_c2) // 2) for three in clast]

mi_vitals = pd.MultiIndex.from_arrays([vitals_c0, vitals_c1, vitals_c2, vitals_c3])
vitals_df = pd.DataFrame(index = Municipios, columns = mi_vitals)

mi.append(mi_vitals)


# Hogar y Vivienda. 
df = sonora[mun][12].copy()
df, extra_home = format_df(df)

c0 = list(df.index)
home_one = [last for j in range(len(c0)) for last in clast]
home_zero = [one for one in c0 for j in range(len(clast))]


mi_home = pd.MultiIndex.from_arrays([home_zero, home_one])
home_df = pd.DataFrame(index = Municipios, columns=mi_home)

mi.append(mi_home)


# Medio Ambiente
df = sonora[mun][13].copy()
df, extra_eco = format_df(df)

c0 = list(df.index)
c0[0] = c0[0].replace('\n', ' ')
eco_one = [last for j in range(len(c0)) for last in clast]
eco_zero = [one for one in c0 for j in range(len(clast))]

mi_eco = pd.MultiIndex.from_arrays([eco_zero, eco_one])
eco2020_df = pd.DataFrame(index = Municipios, columns= mi_eco)

mi.append(mi_eco)


# Salud

health_c0 = ["Servicios de Salud (1)", "Servicios de Salud (1)", "Servicios de Salud (1)", "Servicios de Salud (1)",
             "Tasa de mortalidad", "Tasa de mortalidad", "Tasa de mortalidad infantil", "Tasa de mortalidad infantil",
             "Unidades médicas", "Unidades médicas", "Unidades de consulta externa", "Unidades de consulta externa",
             "Unidades de hospitalización", "Unidades de hospitalización", "Unidades de hospitalización", "Unidades de hospitalización"]
health_c1 = ["Población Afiliada", "Población Afiliada", "Poblacion Usuaria", "Poblacion Usuaria",
             "","","","",
             "", "", "", "",
             "General", "General", "Especializada", "Especializada"]

health_c2 = [last for j in range(len(health_c1) // 2 ) for last in clast]
mi_health = pd.MultiIndex.from_arrays([health_c0, health_c1, health_c2])
health_df = pd.DataFrame(index = Municipios, columns= mi_health)

mi.append(mi_health)

# Seguridad
df = sonora[mun][20].copy()
df = df.set_index(df.columns[0]).replace({"nan":pd.NA}).dropna(axis = 1, how = 'all')
data = df.iloc[1]

seg_one = [df.index[0],df.index[0]] 

mi_seg = pd.MultiIndex.from_arrays([seg_one, clast])
seg_df = pd.DataFrame(index = Municipios, columns=mi_seg)

mi.append(mi_seg)


# Ubicación Geográfica. Check

column_two = ['Coordenadas', 'Coordenadas', 'Coordenadas', 'Coordenadas', 'Coordenadas', 'Coordenadas',
               'Colindancias', 'Superficie', 'Superficie', 'Densidad de Poblacion']
subcolumn_two = ['Latitud', 'Latitud', 'Longitud', 'Longitud', 'Altitud', 'Altitud',
                 '','Km^2','', 'Hab/Km^2']
subsubcolumn_two = ['Min (°)', 'Max (°)','Min (°)', 'Max (°)','Min (m)', 'Max (m)',
                    '','Absoluto', 'Porcentaje','Absoluto']
print('Pepino')
mi_geo = pd.MultiIndex.from_arrays([column_two, subcolumn_two, subsubcolumn_two])
geoson_df = pd.DataFrame(columns=mi_geo, index = Municipios)

mi.append(mi_geo)  # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
