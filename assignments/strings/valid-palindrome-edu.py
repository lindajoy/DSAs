def is_Valid_palindrome(s):
    # Initializing the left and right pointer
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right =  right - 1

    return True


print(is_Valid_palindrome('racecar'))
print(is_Valid_palindrome('tart'))

"""
Time Complexity is O(N) => n being the length of the array

Space Complexity is 0(1)
"""