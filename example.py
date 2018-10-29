__author__ = 'Galo Castillo'

import pandas as pd
from pandas import Series, DataFrame
# matplotlib es para visualizaciones
import matplotlib.pyplot as plt
import numpy as np

# Con esto abro un CSV. La variable 'bebidas' es el tipo de dato DataFrame. Los DataFrame son como tablas que tienen cabeceras.
bebidas = pd.read_csv("bebidas.csv")
# Imprimo los 2 primeros registros del DataFrame
print(bebidas.head(2))
# Imprimo informacion descriptiva de cada columna del DataFrame
print(bebidas.describe())

#Imprimo los nombres de las cabeceras
print(bebidas.columns)

# Imprimo el numero de registros (filas) que tiene el DataFrame
print(len(bebidas))

# Prmero indexo las columnas continent y beer_servings. Luego agrupo los registros por continent y 
# obtengo la media de beer_servings por grupo
print(bebidas[['continent', 'beer_servings']].groupby('continent').mean())

# Prmero indexo las columnas continent y beer_servings. Luego agrupo los registros por continent y 
# obtengo la cantidad de registros por grupo
print(bebidas[['continent', 'beer_servings']].groupby('continent').count())

# Creo la columna total_servings a partir de la suma de los valores de otras columnas.
bebidas['total_servings'] = bebidas['beer_servings'] + bebidas['spirit_servings'] + bebidas['wine_servings']

df = bebidas[['continent', 'total_servings']].groupby('continent')

x = bebidas.groupby('continent')['total_servings'].apply(lambda x: Series({'max': x.max(), 'min': x.min(), 'range': x.max()-x.min()}))
print(x.ix[0,:])

# Prmero indexo las columnas continents y beer_servings. Agrupo por continent y obtengo la media de los grupos.
# Finalmente, hago una gráfico de barras (por eso es kind='bar')
bebidas[['continent','beer_servings']].groupby('continent').mean().plot(kind='bar', title='Beer Servings per Continent')

# Diagrama de cajas
bebidas.boxplot(column='beer_servings', by ='continent')

# Diagrama de cajas
bebidas.boxplot(column='wine_servings', by ='continent')

colors = np.where(bebidas.continent=='EU', 'r', 'b')
bebidas.plot(x='beer_servings', y='wine_servings', kind = 'scatter', alpha = 0.3, c = colors)
plt.show()

df =bebidas[['continent', 'beer_servings']].groupby("continent").agg(['mean', lambda x: x.max()-x.min()])
print(df)


