__author__ = 'LEONARDO'

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import numpy as np

diab = pd.read_csv("diabetes.csv", index_col=0)    # index_col=0 representa que la primera columna quiero que la utilice como indice

diab['tipo'] = diab['age'].apply(lambda i: i//10)
print(diab.head(2))

group = diab.groupby('tipo')
print(group['bmi'].sum()/group['bmi'].count())


mediana = diab['bmi'].median()
#print(mediana)

print(len(diab['bmi'][diab['bmi'] > 25]))

diab["bmi"].plot(kind="kde")
plt.show()



df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(),
                    'size': list('SSMMMLL'),
                    'weight': [8, 10, 11, 1, 20, 12, 12],
                    'adult' : [False]*5 + [True]*2})
grouped = df.groupby('animal')
print(grouped.groups)
print(grouped.size())
print(grouped.sum())


#print(df)
#print(grouped)




