"""
💡 List Comprehensions

Syntax for list comprehenesions: [expression for member in iterable]
"""
"""
EXAMPLE 1

This is a normal function that loops over the range of the numbers in the list and returns the square of each number
squares = []

for i in range(10):
    squares.append(i * i)
"""
# Example 1 -> Implemented as list comprehension

squares = [i * i for i in range(10)]
squares

# Example 2 -> List Comprehension 2
txns = [1.09, 23.56, 56.86, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = [get_price_with_tax(i) for i in txns]
print(final_prices)

# Supercharging Your List Comprehensions
# new_list = [expression for member in iterable]
# Its possible to use conditionals in list comprehensions:

sentence = "the rocket came back from mars"
print("Here's the first word in the sentence:", sentence[0])
vowels = [i for i in sentence if i in 'aeiou']
print(vowels)

# Complex Filters
sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonanats = [i for i in sentence if is_consonant(i)]
print(consonanats)

# Original prices
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)

# Orginal prices 2
# Separate into a function
def get_price(price):
    return price if price > 0 else 0

# print prices
prices = [get_price(i) for i in original_prices]
print(prices)

"""
💡 Set Comprehensions
   A set comprehension is almost exactly the same as the list in Python.
   The only difference is that set comprehensions makes sure the output contains no duplicates.
"""

quote = "life, uh, finds a way"
unique_vowels = { i for i in quote if i in 'aeiou'}
print(unique_vowels)

"""
💡 Walrus Operator
   Say you need to make ten requests to an API that will return temparature data.
   You only want to return results that are greater than 100 degrees Fahrenheit.
   Assume that each request will return different data.

   In this case, there's no way to use a list comprehension in Python to solve the problem. 
   The formula expression for member in iterable(if conditional) provides no way for the conditional to assign data to 
   a variable  that the expression can access

   The walrus operator solves this problem  - It allows you to run an expression while simultaneously assigning the output 
   value to a variable.
"""

import random

def get_weather_data():
    return random.randrange(90,110)

hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print("Here is the array of hot temps:", hot_temps)

"""
As a rule of thumb, it is best to avoid more than one nested comprehensions and use convectional loops
"""
