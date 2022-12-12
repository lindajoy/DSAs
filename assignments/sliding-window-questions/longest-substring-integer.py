'''
Given a string s and an integer k, 
return the length of the longest substring of s that contains at most k distinct characters

🧐 Analysis

𐃉 Distinct means different.
𐃉 A substring - a contiguous(continuous) sequence of characters present within a string. 
                   It is a string present inside a string.

𐃉 Whenever you hear the word contingous thinking of the sliding window.

👻 Example 1:
   input = 'eceba' , k = 2
   Output: 3
   Explanation: The substring 'ece' with length 3

👻 Example 2:
   input = 'aa' , k = 1
   output: 2
   Explanation: The substring 'aa' with length 2

The inputs are string and integer(k)
The output is The length of substring with unique characters

'''

'''
💡 Naive approach.
   1. C
'''

randomString = 'hello'
print(len(randomString))

def getDistinctCharacters(str: str, k: int) -> int:
    charSet = set()
    leftWindow = 0
    res = 0

    for char in range(len(str)):
        while str[char] not in charSet:
            if len(charSet) == k:
                return charSet
            else:
                leftWindow+=1
                return charSet
        return charSet

print(getDistinctCharacters('eceba', 2))


                

    

