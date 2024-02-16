# Creating / Initializing a dictionary can be done in two ways
dict_one = dict()
dict_two = {}

# Populating the dictionary
# 💡 METHOD 1

dict_two["name"] = "Joy Lidah Wawira"
print(dict_two)

# 💡 METHOD 2
dict_one = {"name", "Kekeli Oluoch"}
print(dict_one)

# 💡 METHOD 3 => KeyWord argument list
dict_three = dict(age = "21", month = "July")
print(dict_two)

# PYTHON DICTIONARY METHODS.

# Update Function

harry_potter_chars = {
    "Harry Potter" : "Gryfindor",
    "Albus Dumbledore": "Gryfindor",
    "Cedric Malfoy" : "Slytherin",
    "Helena RavenClaw": "RavenClaw",
    "Hermoinine Granger" : "Gryfindor",
}

print('😫',harry_potter_chars)

another_set_of_harry_potter_chars = {
    "Helena RavenClaw": "RavenClaw",
    "Hermoinine Granger" : "Gryfindor",
}

print('😇', another_set_of_harry_potter_chars)

# TO BE INVESTIGATED
merged_dict = harry_potter_chars.update(another_set_of_harry_potter_chars)

print('❌', merged_dict)

# Delete a key -value pair in a dictionary
del harry_potter_chars["Helena RavenClaw"]

print("Update after Deletion:", harry_potter_chars)

# Popping Items on a dictionary
harry_potter_chars.popitem() # Removes the last element from the dictionary.
print('POP ITEM',harry_potter_chars)
harry_potter_chars.pop("Cedric Malfoy")  # Removes the specific string entered.
print('POP METHOD',harry_potter_chars)

# Getting methods from a dictionary
print(harry_potter_chars.get("Harry Potter"))
print(harry_potter_chars["Harry Potter"])
# print(harry_potter_chars["Cedric Malfoy"])

# items(), keys() and values in dictionaries
print(harry_potter_chars.keys())
print(harry_potter_chars.items())
# print(harry_potter_chars.values())

# 🔁 🔁 Looping through values in dictionaries

for key, value in harry_potter_chars.items():
    print (f"{key}: {value}")

for key_value in harry_potter_chars.items():
    print('🔓',key_value)

for value in harry_potter_chars.values():
    print('😶',value)

for key in harry_potter_chars.keys():
    print('🔑',key)

# Calculating the frequency of each Value in a dictionary
from collections import Counter

# frequency of values
counter = Counter(harry_potter_chars.values())
print(counter)

counter2 = Counter('hellojoy')
print(counter2)


# Enumerate Function: Say you want to loop through an entire list and get its index and count
my_list = [1,2,3,4,5,6,7,8,9]

for index, item in enumerate(my_list):
    print(index ,':', item)

# Something cool I found: Question was on finding the unique character in a string:

for index, value in enumerate(harry_potter_chars.items()):
    print('😁🥹', index ,':', value)

# Lets do some sorting of my dictionary
lord_of_rings_chars = {
    'Aaaragon': 43,
    "Frodo": 89,
    "Samwise": 13,
    "Pippin": 40,
    "Legolas": 30,
    "Gandalf": 90
}

sorted_dictionary_chars = sorted(lord_of_rings_chars.items())
sorted_characters = sorted(lord_of_rings_chars.items(), key=lambda x: x[1], reverse=True)

print(sorted_characters)
print(sorted_dictionary_chars)

