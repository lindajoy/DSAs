"""
Write a function that takes in a string of lowercase English-alphabet letters and returns the index of the string's first non-repeating character.
The first non-repeating character is the first character in a string that occurs only once.
If the input string doesn't have any non-repeating characters, your function should return -1.
"""
sample_string = "abcdcaf"
output = 1

# Input: string
# Output: Index
def firstNonRepeatingCharacter(sample_string):
    if not sample_string:
        return -1
    
    for i in range(len(sample_string)):
        # Used the slicing concept.
        # Example 1:
        # If i am at index 1, I would like to check whether the rest of my string does not have the string within it.
        # So we slice from index 2.
        if sample_string[i] not in sample_string[i+1:]:
            return i
    return -1

print(firstNonRepeatingCharacter(sample_string))
