"""
FIRST NON REPEATING CHARACTER.

Write a function that takes in a string of lowercase English-alphabet letters 
and returns the index of the string's first non-repeating character.

The first non-repeating character is the first character in a string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.

"""

# string = "abcdcaf"
# output = 1

def first_non_repeating_charcter(string):
    freq_chars = {}

    for i in string:
        freq_chars[i] = freq_chars.get(i, 0) + 1

    values = [key for key,val in freq_chars.items() if val == 1]

    indexes = min(string.index(i) for i in values)
    return indexes

print(first_non_repeating_charcter("abcdcaf"))
print(first_non_repeating_charcter("leetcode"))
print(first_non_repeating_charcter("geeksforgeeks"))
print(first_non_repeating_charcter("algorithm"))

    