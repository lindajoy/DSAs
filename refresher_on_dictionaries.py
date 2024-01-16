"""
DICTIONARY:
    Key => The desired key to lookup
    Value => The value set or return

A dictionary is a key value store is also known as Mapping.
It allows you to store and retrieve elements by referencing a key.
As dictionaries are referenced by key, they have very fast lookups.
As they are primarily used for referencing items by key, they are not sorted
"""

# 💡 Creating a Dict
empty_dict = {}
dict_with_initial_values = {'Joy': 'Wawira'}

# Creates a dictionary: Square Dictionary  🤔
square_dict = {num: num*num for num in range(1, 11)}
print('Here is my square dictionary:', square_dict)

# Adding items to a dictionary.
countries = {}
countries['Kenya'] = 'Nairobi'
countries['Tanzania'] = 'Arusha'
print('Countries Dictionary:', countries)

# Its possible to add a list and a dictionary as a value

countries['Lord Of Rings'] = ["Mordor", "Rohan", "Rivendell"]
print("Added lord of rings to countries", countries)

countries['Harry Potter'] = {"Diagon Alley" : "The Burrow"}
print('Added a Dictionary To Harry Potter', countries)

# Deleting an  item from a dictionary, we use the key:
del countries['Harry Potter']
print('Just deleted Harry Potter From Dict', countries)


# 💡 Avoiding KeyError exception
random_dict = {}
# 💡 Throws a KeyError Exception.
# random_dict['not there']

# 💡 Iterating over a dictionary
for key in countries:
    print(key ,':' ,countries[key])

# The same is true when used in a comprehension
print([key for key in countries])

# The items method can be used to loop over both the key and value simultaneously
for key, value in countries.items():
    print('Used items() method:',key, ':', value)

# Whule the values method can be used to iterate over only the values
for value in countries.values():
    print('Calling on the values() method:', value)


# Dictionary with default values
from collections import defaultdict

default_dictionary = defaultdict(int)
default_dictionary['key'] = 5
default_dictionary['key'] = 5
print('Default dictionary: ',default_dictionary)

# Merging Dictionaries
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
print({**fish, **dog})

# As this example demonstrates, duplicate keys map to their lattermost value (for example "Clifford" overrides "Nemo").

# 💡 ACCESSING VALUES OF A DICTIONARY
access_dict = {"Hello": 1234, "World": 1900}
print(access_dict['Hello'])

# Using the get syntax: dictionary.get(keyname, value)
my_dict = {"apple": 2, "banana": 3, "orange": 4}
print(my_dict.get("apple"))
print(my_dict.get("apple", 2))

# Zip() function explored.
names = ['Joy', 'Wawira', 'Lidah']
tags = ['Felicitations', 'Kudos', 'Bravo']

for name, tag in zip(names, tags):
    print('🎉 {0} , {1} here is your Google offer letter.'.format(tag, name))
    print('You will be joining Google next week!')




