import pandas as pd
import random

Nationality = pd.Series({'Messi': 'Argentine', 'Ronaldo': 'Portuguese', 'Neymar': 'Brazilian',
                         'S. Roberto': 'Spanish'})


Salary = pd.Series({'Messi': '41 million Euro', 'Ronaldo': '35 million Euro', 'Neymar': '30 million Euro',
                    'S. Roberto': '10 million Euro'})


var = pd.DataFrame({'Nationality': Nationality,
                    'Salary': Salary})

print("Index are ---->> ", var.index)
print("Values are ---->> ", var.values)
print(" ")
print(var.columns) #Nationality and Salary
print(" ")
print(var['Salary']['Messi']) #Accessing Messi's salary
print(var)
print(" ")
print(Nationality) #Just Nationality Index and value
print(" ")
print(Salary) #Just Salary Index and value
print(" ")
print(var.columns[0])
print(Salary[0])

print(pd.DataFrame(Nationality, columns=['Nationality']))

#From a list of dictionaries
data = [{'a': i, 'b': 2 * i} for i in range(3)] # list comprehension
print(pd.DataFrame(data))

#Misising value will print as NaN
missing = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
print(missing)
print(" ")

 # From a two-dimensional NumPy array
# -----------------------------------
