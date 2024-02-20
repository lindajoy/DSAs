# Link to continue reading this: https://freedium.cfd/https://towardsdatascience.com/41-questions-to-test-your-knowledge-of-python-strings-9eb473aa8fe8

# 1. How do you confirm that 2 strings have the same identity
"""
The is operator returns True if 2 names point to the same location in memory, This is what we
are refeering to when we talk about identity

Dont confuse  is with ==, the latter which only tests equality.
"""
animals = ["python", "gopher"]

more_animals = animals
print(id(more_animals))
print(id(animals))

print('Should return True:', animals == more_animals)
print('Should return True:', animals is more_animals)

# How would you check if each word in a string begins with a capital letter

print('The Hilton'.istitle())
print('a lonely night'.istitle())
print('A sad day again'.istitle())

# Check if a string contains a specific substring
print('plane' in "The world's fastest plane")
print('car' in "The world's fastest plane")

# Find the index of the occurence of a substring in  a string
print("The world's fastest plane".find("plane"))
print("The world's fastest plane".index('plane'))

# Count the total number of characters in a string.
len('I am getting into a google')

# Count the number of a specific character in a string
print("After attempting to teach my dog to speak Spanish, all I got in return was a confused look and a bark that sounded suspiciously like '¡Guau!'".count('a'))

# Capitalize the first character of a string
print("florida dolphins".capitalize())

# Using the fstring
name = 'Ann'
second_name = 'Mukami'

# Interpolating a variable
print('{0} , {1} will be the best teacher in the whole world'.format(name, second_name))

# Search a specific part of a string from a substring
print("Why don't skeletons ever fight each other? Because they don't have the guts!".index('the', 10, 50))

# Check if a string contains only numbers
# This should return true
print('8000'.isnumeric())
print('800i'.isnumeric())

# Split a string on a specific character
print("This is great".split(" "))
print("not--so--great".split("--"))
print('yellow@baggins#lish#megan'.split("#"))

# Destructuring
username, domain = "joy@google.com".split("@")
print(username)
print(domain)

# Check if a string is composed of all lower case characters
print("all lower case".islower())
print("not ALL lowercase".islower())

# Check if the first character in a string is lowercase
print('aPPLE'[0].islower())

# Reversing
random_string = "Hotel Transalvaynia"
print(''.join(reversed(random_string)))
print(random_string[::-1])

# Joining a list into a single string
hotel_transylvania_characters = [
    "Dracula",
    "Mavis",
    "Jonathan",
    "Frankenstein",
    "Wayne",
    "Murray",
    "Griffin",
    "Blobby",
    "Ericka Van Helsing",
    "Dennis",
    "Winnie",
    "Quasimodo",
    "Eunice",
    "Tinkles",
    "Belvedere",
    "The Werewolf Kids"
]


my_combined_characters = '-'.join(hotel_transylvania_characters)
print('😄', my_combined_characters)

# Check if all characters in a string conform to ASCII
print('A'.isascii())
print('A'.isascii())
