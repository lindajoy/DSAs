"""
Valid Palindrome 2: https://leetcode.com/problems/valid-palindrome-ii/


"""


def is_valid_palindrome(str):
    i , j = 0, len(str) - 1
    count = 0
    
    while (i < j - 1):
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[i].isalnum() and i < j:
            j -= 1
        if str[i].lower() != str[j].lower():
            count += 1
        if count == 1:
            return False

        i, j = i + 1 , j - 1

    return count


print(is_valid_palindrome('abca'))
# print(is_valid_palindrome('aebcbda'))

# print(is_valid_palindrome('aba'))
# print(is_valid_palindrome('abc'))

"""
Minimum number of charcters that we need to delete make a string a valid palindrome

"""
def minimum_chracters_to_be_deleted(str):
    i , j = 0, len(str) - 1
    count = 0
    
    while (i < j - 1):
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[i].isalnum() and i < j:
            j -= 1
        if str[i].lower() != str[j].lower():
            count += 2
            print(count)



    return count

