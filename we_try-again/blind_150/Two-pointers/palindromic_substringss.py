"""
💡 Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

# Whats the input? A string
# Whats the output? Number of palindromes that can be formed from the string

# 🤔 Initial thoughts

#   i) The obvious answer is that every string initially here is a palindrome
#      Say length of string is 3, the inital number of palindromes is 3

#   ii) Initialize the left and right pointer; they will start at 0 and 1
#       a) If the substring is a palindrome 
#   ii) We can have a helper function that checks whether our string is a palindrome

# Lets look at the example "ababa" the output should be 6:
# Our initial number of palindromes will be 5
# So if we have a left pointer at 0 and the right pointer at 1, Check whether this passes the palidrome:
# 
# right + 1
# else left = right
# right = left +=1

def isPalindromicString(string):
    initial_count = len(string)
    left = 0
    right = left + 1
    count = 0

    if string[::-1] == string:
        initial_count += 1

    while right < len(string):
        sliced_str = string[left: right + 1]
        print(sliced_str)
        print(reversed(sliced_str))
        if sliced_str[::-1] == sliced_str:
            count += 1
            left = right
            right += 1
        else:
            right += 1


    return count + initial_count
print(isPalindromicString('ababa'))


