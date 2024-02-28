"""
SMALLEST INCONSTRUCTIBLE VALUE

Given a set of coins, there are some arnounts of change that you may not be able to make with them, 
e.9., you cannot create a change amount greater than the sum of the your coins.
For example, if your coins are 1,1,1,1,1,5,10,25, then the smallest value of change which cannot be made is 21.
Write a program which takes an array of positive integers 
and retums the smallest number which is not to the sum of a subset of elements of the array.

"""
def small_inconstructible(nums):
    result = 1
    nums.sort()

    for i in nums:
        if i > result:
            break
        result += i
    return result

print(small_inconstructible([1,1,1,1,1,5,10,25]))

