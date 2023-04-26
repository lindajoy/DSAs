"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1

Input: s = "leetcode"
Output: 0

Example 2

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1

Input here is a string, Output is the index of the non-repeating character
"""

'''
Pseudocode here would be:
 1. Here basically we will need to loop through the entire string and generate key value pairs(index: value) =>  Using the enumerate function.
 2. Check if the count of the specific character is equal to 1
 3. Return it
 4. If no character has occured once return -1.

'''
txt = "I love apples, apple are my favorite fruit"
x = txt.count("a")

print(x)

def find_first_unique_character(text:str):
    # Generate key-Value of the index of each charater.
    for i, c in enumerate(text):
        # Counts the number of times a character appears in a string.
        if text.count(c) == 1:
            return i

    return -1


