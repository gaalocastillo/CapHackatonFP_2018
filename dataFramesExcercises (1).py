__author__ = 'LEONARDO'

from pandas import Series, DataFrame
import numpy as np

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

df = DataFrame(data, index =["a", "b", "c", 3, 4])


df = df.sort_values(by=['year', 'pop'])
print(df)
rankSeries = df['pop'].rank(ascending=False, method='max')
print(rankSeries)
df2 = DataFrame(2*np.random.rand(100).reshape(10, 10)-1, columns=list('abcdefghij'))
print(((df2.describe()).ix[['min', 'max', 'mean'], :]).transpose())
print(df2)

lista = list('abcdefghij')
min = (df2.describe()).ix['min']
max = (df2.describe()).ix['max']
mean = (df2.describe()).ix['mean']
counter = []
for j in lista:
    cont = 0
    for i in range(0,10):
        if df2.ix[i, j] > 0:
            cont += 1
    counter.append(cont)
dict = {'min': min, 'max': max, 'mean': mean, "count": counter}
df3 = DataFrame(dict)
print(df3)
