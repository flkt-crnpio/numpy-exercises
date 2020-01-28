# Pandas is an open source python library providing high performance data manipulation
# and analysis tool using powerful data structures.
# The name Pandas is derived from the word Panel Data - an Econometrics from Multidimensional data.

# Pandas have this data structures that are built on top of Numpy arrays
#   * Series
#   * DataFrame
#   * Panel

# pandas.DataFrame
# class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# Two-dimensional size-mutable, potentially heterogeneous tabular data structure
# with labeled axes (rows and columns). Arithmetic operations align on both row and column labels.
# Can be thought of as a dict-like container for Series objects. The primary pandas data structure.
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd

my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

cars = pd.DataFrame(data=my_dict)

print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
