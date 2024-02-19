"""
Write a program which takes a nonnegative integer and retums the largest integer whose square is less than or equal to the given integer. 
For example, if the input is 16, return 4; if the input is 300, return 17, since 17 * 17 = 289 < 300 and 18 = 324 > 300.
"""

# Whats the input? An integer k

# Who would ever think that this would equate to a binary search solution.

def square_root(k):
    # Initialize the left and the right pointer.
    # Left is initialized to 0
    # While right is set to k
    left, right = 0, k

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

print(square_root(289))
        