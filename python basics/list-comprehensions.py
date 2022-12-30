# From Educative => List comprehensions.

letters = "python"

alphabets = [letter for letter in letters]

print(alphabets)

# instead of:

alphabets2 = []

for letter in letters:
    alphabets2.append(letter)

print(alphabets2)

# Filtering with list comprehensions
numbers = [1,2,3,3,5,6,8,10]

even_numbers = [number for number in numbers if number%2 == 0]

print(even_numbers)


# Enriched iterations with list comprehensions
# You can also use list comprehensions with nested for loops.
# This bit we are creating a tuple from each list.

even = [2,4,6,8,10]
odd = [1,3,5,7,9]

pair = []
for number1 in even:  # Taking every number from even
    for number2 in odd: # Taking every number from odd
        pair.append((number1, number2)) # Pairing every number from even with every number from odd

print(pair)


# List comprehension
# tuple

pair2 = [(number1,number2) for number1 in even for number2 in odd]
print(pair2)
