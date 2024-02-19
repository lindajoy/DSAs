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