"""
HASHSET // DICTIONARY: Key/ Value Pairs

Question:

Given a string, pal_string, consisting of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

NOTE: Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

def LongestPalindrome(str):
    freqDict = {}
    pal_string = ""
    odd = False

    for s in range(len(str)):
        if str[s] in freqDict:
            freqDict[str[s]] += 1
        else:
            freqDict[str[s]] = 1

    for s in str:
        if freqDict[s] % 2 == 0:
            pal_string += s
        elif odd != True:
            odd = True
            pal_string += s

    return len(pal_string)


print(LongestPalindrome('abccccdd'))
print(" o" + "l")