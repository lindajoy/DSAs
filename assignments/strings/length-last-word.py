"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

"""
How do you remove spaces from a text?

"""

"""
💡 Add check if the characters contain a number: Pop them
"""
random_sentence = "luffy is still joyboy23!ß"

def lengthOfLongestString(random_sentence):
   random_array = [len(i) for i in random_sentence.split() if i.isalnum()]
   print('😁 👀', random_array)
   return random_array[-1]

print(lengthOfLongestString(random_sentence))