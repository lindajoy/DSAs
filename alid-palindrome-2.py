"""
Valid Palindrome 2: https://leetcode.com/problems/valid-palindrome-ii/
"""


def is_valid_palindrome(str):
    i , j = 0, len(str) - 1
    count = 0
    
    while i < j:
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[i].isalnum() and i < j:
            j -= 1
        if str[i].lower() != str[j].lower():
            count += 1
        if count == 1:
            return True

        i, j = i + 1 , j - 1

    return False


print(is_valid_palindrome('aba'))
