# DICTIONARY

# A dictionary is an example of a key value store  also known as a mapping in Python.

# It allows you to store and retrieve elements by refrencing a key. Dictionaries are referenced by keys, they have very fast lookups.

# Creating a dictionary

d = {}  # Creates an empty dict
d = { "key" : "value"} # dict with initial values

# makes a shallow copy of otherdict
# d = {**otherdict}

# also updates the shallow copy with the contents of the yetanotherdict.

# d = {**otherdict, **yetanotherdict}

# Dict comprehension => This is interesting!
d = {k:v for k, v in [{'key', 'value'}]}


my_dictionary = {}

# Adding a new element/s to my dictionary
my_dictionary["Joy"] = 24
my_dictionary['Joan'] = 37
my_dictionary['Lidah'] = 19
my_dictionary['Mwenda'] = 18
my_dictionary['Mukami'] = 14
my_dictionary["Sarah"] = 37
my_dictionary["Vincent"] = 50
my_dictionary["Milah"] = 60

print("My full dictionary:", my_dictionary)

# Removing an element from the dictionary
del my_dictionary['Milah']
print("Deleted Milah:", my_dictionary)

# Also possible to add a list and dictionary as value.
my_dictionary["jobs"] = ["Engineer", 'Doctor', 'Pilot',"Captain", 'Teacher', "Awesome Mother", "Awesome Father"]
print("Added Jobs as key to my dictionary:", my_dictionary)