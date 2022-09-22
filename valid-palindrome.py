"""
Valid Palindrome: https://leetcode.com/problems/valid-palindrome/
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
print(''.join(reversed('mom')))

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