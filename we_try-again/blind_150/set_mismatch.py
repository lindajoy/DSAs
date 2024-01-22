for i in range(1, 6):
    print(i)

"""
SET MISMATCH

You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""

"""
QUESTION FOR INTERVIEWER:
    1. When you say repitition we always mean that the number will always be repeated twice, not thrice?
    2. 
"""

from collections import Counter

def setMisMatch(nums):
    res = [0, 0] #duplicate, missing

    count = Counter(nums)
    print('First count',count)

    for i in range(1, len(nums) + 1):
        if count[i] == 0:
            res[1] = i
        
        if count[i] == 2:
            res[0] = i
    return res

print(setMisMatch([1,2,2,4]))


# Instead of using counter you can create a dictionary yourself
def setMisMatch2(nums):
    res = [0,0]
    count_dict = {}

    # Here we are creating a dictionary
    for i in nums:
        count_dict[i] = count_dict.get(i, 0) + 1

    print('Second counter', count_dict)

    for i in range(1, len(nums) + 1):
        if i not in count_dict:
            res[1] = i
        elif count_dict[i] == 2:
            res[0] = i

    return res

print(setMisMatch2([1,2,2,4]))

# Lets try something
numbers = [1,2,3,5,5,7,6,9]
count_of_number = Counter(numbers)
print("Count of numbers", count_of_number)
list_zeros = []
for i in range(1, len(numbers) + 1):
    if count_of_number[i] == 0:
        list_zeros.append(i)

print(list_zeros) 

# Random lets create a dictionary manually
random_count = {}
list_zeros_2 = []

for num in numbers:
    random_count[num] = random_count.get(num, 0) + 1

print('Created Dictionary Manually', random_count)
for i in range(1, len(numbers) + 1):
    if i not in random_count:
        list_zeros_2.append(i)

print(list_zeros_2)


# Last example on dictionaries.
random_count_2 = {}
list_zeros_3 = []

for num in numbers:
    if num in random_count_2:
        random_count_2[num] += 1
    else:
        random_count_2[num] = 1

for i in range(1, len(numbers) + 1):
    if i not in random_count_2:
        list_zeros_3.append(i)

print('My random count:',random_count_2)
print('My random count:',list_zeros_3)






