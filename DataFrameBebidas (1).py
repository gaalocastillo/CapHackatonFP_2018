__author__ = 'LEONARDO'

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

bebidas = pd.read_csv("bebidas.csv")
print(bebidas.head(2))
print(bebidas.describe())

#print(bebidas[['continent', 'beer_servings']].groupby('continent').mean())

#print(bebidas[['continent', 'beer_servings']].groupby('continent').count())

bebidas['total_servings'] = bebidas['beer_servings'] + bebidas['spirit_servings'] + bebidas['wine_servings']

#df = bebidas[['continent', 'total_servings']].groupby('continent')

x = bebidas.groupby('continent')['total_servings'].apply(lambda x: Series({'max': x.max(), 'min': x.min(), 'range': x.max()-x.min()}))
print(x.ix[0,:])

#bebidas[['continent','beer_servings']].groupby('continent').mean().plot(kind='bar', title='Beer Servings per Continent')

#bebidas.boxplot(column='beer_servings', by ='continent')

#bebidas.boxplot(column='wine_servings', by ='continent')

#colors = np.where(bebidas.continent=='EU', 'r', 'b')
#bebidas.plot(x='beer_servings', y='wine_servings', kind = 'scatter', alpha = 0.3, c = colors)
#plt.show()

#df =bebidas[['continent', 'beer_servings']].groupby("continent").agg(['mean', lambda x: x.max()-x.min()])
#print(df)


