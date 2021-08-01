dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ['1','2','3','4','5']
print(brics)

cars = pd.read_csv('test.csv')
# cars.index = ['1']
print(cars)
print()
print(cars[['b']])

print()

print(cars[['a','b']])

print()

print(cars['a'])


print()




val = pd.read_csv('test.csv')
# print(val)
print(val[0:4])

print()

print(val[1:2])

print()


print(val.iloc[0])

print()
print(val.loc[['a', '1']])
