"""
Valid Palindrome: https://leetcode.com/problems/valid-palindrome/

Python methods learnt from this are :
       1.isalnum() returns true if all the characters are alphanumeric
         (a-z) and (0-9) are alphanumeric
       2. lower() returns a string in lower case
"""

"""
💡 First attempt: Works with strings with no punctuation marks😊
"""
def is_palindrome(str):
    b = ''.join(reversed(str))
    print(b)
    if str == b:
       return True
    else:
        return False

print(is_palindrome('mom'))

"""
💡 Second attempt : Lets mimick the first step but remove the punctuation marks
"""

def is_palindrome_two(str):
    c = reversed(str)
    a = ''.join(ch for ch in c if ch.isalnum())
    d = ''.join(ch for ch in str if ch.isalnum())
    print(a)
    if a.lower() == d.lower():
        return True
    else:
        return False


print(is_palindrome_two("Mr. Owl ate my metal worm"))

"""
The first and second attempt work but they are not better in saving the space complexity since for both operations 
we need to save the reversed strings in another variable!
"""

"""
💡 Third attempt: Optimal Solution.
  Saves on Time and Space complexity!
"""

def is_palindrome_three(str):
    i, j = 0, len(str) - 1

    while i < j:
        while not str[i].isalnum() and i < j:
            i += 1
        while not str[i].isalnum() and i < j:
            j -= 1
        if str[i].lower() != str[j].lower():
            return False

        i, j = i + 1 , j - 1

    return True

print(is_palindrome_three('Dont nod'))