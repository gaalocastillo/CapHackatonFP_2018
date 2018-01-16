__author__ = 'LEONARDO'

import sqlite3
import pandas as pd

con = sqlite3.connect("aapdonation.db")
df = pd.read_sql('SELECT*FROM aapdonate', con, parse_dates=['DATE'])
print(df.head(1))
print
#print(df)
'''
#Donacion Mas Alta
nombre = df[['AMT', 'DATE', 'NAME']].max().NAME
donacion = df[['AMT', 'DATE']].max().AMT
fecha = df[['AMT', 'DATE']].max().DATE

print "Fecha: ", fecha
print "Valor: ", donacion
print "Nombre: ", nombre
print

#Numero de Donaciones
print "Numero de Donaciones:", df['AMT'].count()
print

#Numero de donaciones > 100000
print "Numero De Donaciones mayores a cien mil: ", df['AMT'][df['AMT']>100000].count()
print

#Pra cada estado: Numero de donaciones, total, promedio, ordenadas de mayor a menor.
byState = df[['STATE', 'AMT']].groupby('STATE')
df1 = byState.agg([('Donaciones','count'),('Promedio','mean')])
print(df1['AMT'].sort(['Donaciones']))

#Pra cada pais: Numero de donaciones, total, promedio, ordenadas de mayor a menor.
byCountry = df[['COUNTRY', 'AMT']].groupby('COUNTRY')
df2 = byCountry.agg([('Donaciones','count'),('Promedio','mean')])
print(df2['AMT'].sort(['Donaciones']))
'''
#Detectar Errores en el uso del TID
df3 = (((df[['NAME', 'TID']].groupby('TID')).agg([('Count', 'count')])))
print(df3)
print(len(df3[df3['NAME']['Count']>1]))
#df3['NAME'].sort(['Count'], ascending=False)


