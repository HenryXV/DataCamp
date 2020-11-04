import pandas as pd

# Data
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'names': names, 'dr': dr, 'cpc': cpc}

cars = pd.DataFrame(my_dict)
print(cars)

# List os labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars.index = row_labels
print(cars)
