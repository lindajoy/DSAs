"""
All letters in a string are distinct except for one, which occurs twice. Determine which one.

"""

def repetitiveCharacters(str):
    
    str_set = set()
    lst_repetitive_chars = []

    for i in str:
        if i in str_set:
            lst_repetitive_chars.append(i)
        else:
            str_set.add(i)
    return ''.join(lst_repetitive_chars)

print(repetitiveCharacters('codilityy'))


# Find the missing positive number: You are given an array: 
# Say: [1,2,3,5,2]
# Find the smallest greatest integer that is missing from the array:
# if the number is negative, find the largest positive number.

arr = [1,2,3,5,2]
arr2 = [-1,-2]

def findingMissingNumber(arr):
    # Validate the input
    # is it possible to recieve decimal numbers in our array
    if not arr or len(arr) == 0:
        return 1
    
    # Remove all the duplicate numbers
    arr_set = set(i for i in arr if i > 0)
    if 1 not in arr_set or not arr_set:
        return 1
    
    i = 2

    if i in arr_set:
        i += 1
    return i
import random
random_array = random.sample(range(-1000000, 1000001), 1000000)
print(findingMissingNumber(random_array))


# Given a list of numbers, find the product of two numbers that sum up to the number 3333.
#  Example:
# // Given these numbers:
# // 1033
# // 35
# // 3000
# // 1456
# // 2300
# // 1290

# Assuming that you are given an array: [1033, 35, 3000, 1456, 2300, 1290]
# Using the two pointers method:

arr = [1033, 35, 3000, 1456, 2300, 1290]
sum_of_two = 3333

def findProduct(arr, sum_of_two):
    arr_sorted = sorted(arr)
    left, right = 0, len(arr) - 1

    while left < right:
        if arr_sorted[left] + arr_sorted[right] == sum_of_two:
            print(arr_sorted[left], arr_sorted[right])
            prod =  arr_sorted[left] * arr_sorted[right]
            return prod
        elif arr_sorted[left] + arr_sorted[right] > sum_of_two:
            right -= 1
        else:
            left += 1

print(findProduct(arr, sum_of_two))

        

