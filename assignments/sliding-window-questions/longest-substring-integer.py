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

    while (len(charSet) < k):
        for char in range(len(str)):
            charSet.add(str[char])
            print('Nimefika hapaa')
            return len(charSet)
    else:
        return len(charSet)

print(getDistinctCharacters('eceba', 2))


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

Patt

    

