# Maximum Odd Binary Number.

"""
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number 
is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
Example 2:

Input: s = "0101"
Output: "1001"
Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".
"""

# Cant believe this question was testing on string concatenation

# One thing thats for sure is that for us to achieve an odd number whenever we are given a binary number: 
# We need to add 1 to our last Index

# The question assures us that there will always be one 1.

# String Concatenation.
# This question made me feel stupid 
def maximumOddBinaryNumber(binary):
    count_of_ones = 0

    for i in binary:
        if i == "1":
            count_of_ones += 1

    return (count_of_ones - 1) * "1" + (len(binary) - count_of_ones) * "0" + "1"

random_str = "add(3,4)"

# Intuition of this solution:

# We are looping through the array in reversal, if we find the first 1, we
# Swap them with the last value in our array.
# We later join them to ensure we return a string.

def maximumOddBinaryNumber2(binary):
    # 010 => Sorted would be 100
    sorted_s = sorted(binary, reverse=True)
    print("Sorted S:", sorted_s)

    for i in range(len(binary) - 1, -1, -1):
        if sorted_s[i] == "1":
            print(sorted_s[i])
            print(-1)
            sorted_s[i], sorted_s[-1] = sorted_s[-1], sorted_s[i]
            break
    return ''.join(sorted_s)
print(maximumOddBinaryNumber2("0101"))

def find_sum(r_str):
    # Removing the unecessary parts of a string.
    sliced_str = r_str[4:-1]
    # Splitting by ","
    nums = sliced_str.split(',')

    total = 0
    for i in nums:
        total += int(i)
    return total

print(find_sum("add(3,4)"))





