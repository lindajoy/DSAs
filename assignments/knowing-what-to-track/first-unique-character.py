"""
For a given string of characters, s, your task is to find the first non-repeating character in it and return its index.
Return 1 −1 if there’s no unique character in the given string.
Constraints: All letters are in lowercase.

💡 Example I

str = "Happy Aniversary"
First_unique_character = 0

💡 Example 2
str = "good morning"
First_unique_character = 2 (🤔 Hapa Sijaelewa)

The input in this case is a string and the output is the index of a unique character
"""
"""
Pseudocode: 
    1. Initialize an empty dictionary
    2. Loop through each string character by creating a count for each
    3. Loop through each charset character and return where the value == 1
"""

# Solution 1

def unique_characters(s):
    # Initialize an empty dictionary
    charCount = {}

    for i in range(len(s)):
        if s[i] in charCount:
            charCount[s[i]] += 1
        else:
            charCount[s[i]] = 1


    for i in range(len(s)):
        if charCount[s[i]] == 1:
            return i

    
    return -1

    
print(unique_characters('happy aniversary'))


# Solution 2

"""
=> Using Counter:
Counter is a subclass of dict that’s specially designed for counting hashable objects in Python. 
It’s a dictionary that stores objects as keys and counts as values. To count with Counter, 
you typically provide a sequence or iterable of hashable objects as an argument to the class’s constructor.

(Its a more pythonic way of creating a dictionary from a string)
"""

from collections import Counter


def first_unique_character(s):
    # Using Counter to create a hashable object

    # This one is more optimal with the import Counter 
    # from collections that helps in creating a hashable object.
    count_chars = Counter(s) 

    for i in range(len(s)):
        if count_chars[s[i]] == 1:
            return i

    return -1


print('Second Example' ,first_unique_character('happy aniversary'))


# Solution 3


def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Initialize a right and left pointer
        left = 0
        right = left + 1
        # Sort nums 
        nums2 = nums.sort()
        print(nums2)

        print(len(nums2))

        while right < len(nums2):
            if nums2[left] == nums2[right]:
                return True
            else:
                left += 2
                right = left + 1

        return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))
