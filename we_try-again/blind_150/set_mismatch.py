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

