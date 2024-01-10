"""
Write a function that takes in two non-empty arrays of integers, f
inds the pair of numbers (one from each array) whose absolute difference is closest to zero, 
and returns an array containing these two numbers, with the number from the first array in the first position.
Note that the absolute difference of two integers is the distance between them on the real number line. 
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]
"""

# 💡 For this we use the two pointers approach.
# 💡 Whats is the input? 2 arrays
# 💡 What's the output? A pair (that when subtracted by each is close to zero).

# Say if i had something like:
#  Input: [2,4,8,1,3,12], [13,14,12,1,19]
#  Output should be (1, 1) because when 1 is subtracted from one becomes 0

def smallest_difference(arrayOne, arrayTwo):
    # We will start by sorting the arrays.
    arrayOne.sort()
    arrayTwo.sort()

    # Initalize variables that are needed.
    idx_one, idx_two = 0, 0
    smallest_difference = float('inf')
    result = []

    # Loop using a while loop
    while idx_one < len(arrayOne) and idx_two < len(arrayTwo):
        number_one = arrayOne[idx_one]
        number_two = arrayTwo[idx_two]

        current_difference = abs(number_one - number_two)

        if current_difference == 0:
            return [number_one, number_two]
        
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            result = [number_one, number_two]

        if number_one < number_two:
            idx_one += 1
        else:
            idx_two += 1

    return result

arrayOne_2 = [1, 3, 5, 7]
arrayTwo_2 = [2, 4, 6, 8]
# Expected output: [1, 2]

# Test Case 3
arrayOne_3 = [4, 8, 15, 28]
arrayTwo_3 = [7, 10, 16, 22]

print(smallest_difference(arrayOne_2, arrayTwo_2))
        