"""
TEST FOR PALINDROMIC PERMUTATION.

A palindrome is a string that reads the same forvrrards and backwards, e.g., "level", "rotator", and "foobaraboof".
Write a program to test whether the letters forming a string can be permuted to form a palindrome. 
For example, "edified" can be permuted to form "deified".
"""

# Whats the Input? A string
# Whats the Output? Returns a True or False if the string given can make a palindromic string

# Something to note is that when we are forming a palindrome:
# Say we had "aba": 
# To investigate whether the string can form a palindrome or not,
# We need to create a hashmap that counts the number a specific character has occured in our string
# When we add all the occurences the total should be equal or less than one.

def  can_form_palindrome(s):
    count_dict = {}

    for i in  s:
        count_dict[i] = count_dict.get(i, 0) + 1

    total_sum = 0

    for i in count_dict.values():
        total_sum += i % 2


    return True if total_sum <= 1 else False

print(can_form_palindrome("aba"))
print(can_form_palindrome("edified"))
print(can_form_palindrome("abccd"))