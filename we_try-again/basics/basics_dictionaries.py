"""
Dictionary:

Comprises of two parameters:
1. key => The desired key to lookup
2. value => The value set or return
"""

# 1. Creating a Dictionary
d = {}

d = {"Joy": "Engineer"}

# Making a shallow copy of another dict

otherdict = {'Mukami': "Sister"}
shallow_copy = {**otherdict}
print('Here is my shallow copy:', shallow_copy)

# Updates the shallow copy with contents of another dict
combination_copy = {**otherdict, **d}
print("Combined copy", combination_copy)

# Dict comprehension
dict_comprehension = {k:v for k, v in [('key', 'value',)]}

dummy_dict = dict()
dummy_dict = dict(Joy='London')
dummy_dict = dict([('Wawira','Canada'),('Mwenda','USA') ])

# Prints out items and the keys in the dictionary;

# for i in dummy_dict.keys():
    # print('Keys',i)

# for i in dummy_dict.items():
    # print('Items', i)

dummy_dict['Mukami'] = 'Inglewood'
dummy_dict['Ann'] = 'Siberia'

print('Updated dummy dict', dummy_dict)

# Delete an item from a dictionary

del dummy_dict['Mwenda']

print(dummy_dict)

# Iterating over a dictionary:

random_dict = {'Ann': 'Siberia','Wawira': 'Canada', 'Mwenda': 'USA', 'Mukami': 'Inglewood' }

for key in random_dict:
    print('Hello i am ',key, 'and I live in', random_dict[key])


# Dictionary with default values
from collections import defaultdict

d_int = defaultdict(int)
d_int['boom'] = 1
d_int['key'] = 5
# print(d_int)

d_str = defaultdict(lambda: 'empty')
# print(d_str)

# Merging Dictionaries

movie_1 = {'name': 'Past Lives', 'actor1' : 'Nora', 'actor2': 'Hae Jung'}
movie_2 = {'name': 'Zootopia', 'actor1': 'Juddy', 'actor2': 'Fox'}

# So it does not really merge the two dictionaries, it just returns the latermost values from the dictionary
movies_combined = {**movie_1, **movie_2}
print(movies_combined)