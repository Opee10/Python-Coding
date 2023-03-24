import pandas as pd

#another to of series object. It's kind of best way cuz it's more clear
population_dict = {'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series(population_dict) # Converted to pandas series object
print(population)

country = pd.Series(['Dhaka', 'Oval', 'New York', 'Venice'] , index = ['Bangladesh', 'London', 'USA', 'Italy'])
print(country)
print(country['Bangladesh'])