"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
Input = [7, 3, 2, 9]
Output = [7, 3, 3, 0]

Input2 = [5, 6, 7, 8, 9]
Output = [5, 6, 7, 9, 0]

# Am the one who is not getting this? 🤔
def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

print(plusOne(Input2))

numbers = [1,2,3,4,5,6,6,7,8,9]

# Traversing the array in reversal.
# The array of numbers!
for i in range(len(numbers) - 1, -1, -1):
    print('😮‍💨 Random Index', i)

# ==== BREAKDOWN OF THE PLUS ONE PROBLEM ====
# So you are given an array of numbers and you are asked to add a one
my_random_numbers = [1,2,3,4,5]
my_random_numbers2 = [1,2,3,4,9]

def plusOneBreakDown(digits):
    for i in range(len(digits) - 1, -1, -1):
        # If the most significant digit was 9 then we need to carry over a one
        if digits[i] == 9:
            digits[i] = 0
        else:
        # Else we just need to add one
            digits[i] = digits[i] + 1
            return digits
        # This means that our number was 9, and was set to zero
        # a new digit 1 is added at the beginning of the array to represent the carry.
    return [1] + digits

print('My random Numbers(Addition Plus one)', plusOneBreakDown(my_random_numbers2))

# I am thinking about indexing
random_string_add = "add(14,15)"
# Converting it to a string
print(random_string_add[4 : -1].split(','))
random_string_joy = "hufflepuff"
print(random_string_joy[6: ])

# Interesting way of doing this ~ Hmm 🤔
# Another implementation of Plus One
def plus_one_one(A):
    # Add the last integer in the array plus one.
    A[-1] += 1
    print('Hmm Discovering Something:', A)
    for i in reversed(range(1, len(A))):
        print(i)
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A

print(plus_one_one([1,2,3,9]))

for i in reversed(range(1, len([1,2,3,9]))):
    print('Index at I', i)

