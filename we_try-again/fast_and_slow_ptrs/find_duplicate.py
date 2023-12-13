"""
Given an unsorted array of positive numbers, nums, such that the values lie in the range [1,n]
,inclusive, and that there are n+1 numbers in the array, find and return the duplicate number present in nums. 
There is only one repeated number in nums.

Note: You cannot modify the given array nums. You have to solve the problem using constant extra space.
"""
"""
SAMPLE EXAMPLE 1

Input: [1,3,3,4,2,5]
Output: 3

SAMPLE EXAMPLE 2

Input: [1,5,3,4,2,5]
Output: 5
"""
# ===> MIND BLOWING 🤯🤯

# Something to note in this question is that there is only one repeated number in nums.
# 💡 So whenever, we are just looking for one number 🤔
# The best solution would be to use a set and find the duplicate.

# But I think the trick here is, You cannot modify the array itself, 
# You have to solve the problem using only extra space!!!

# Discovering that you can use Fast and slow pointers in this question..

def find_duplicate(nums):
    # Initialize the fast and slow pointers and make them point the first element of the array.
    fast = slow = nums[0]

    while True:
        # Move the slow pointer using the nums[slow] flow
        slow = nums[slow]

        # Move the fast pointer two times faster as the slow pointer
        fast = nums[nums[fast]]

        # Break the loop when the slow pointer becomes equal to the first pointer
        if slow == fast:
            break

    # Part # 2
    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast

print(find_duplicate([1,5,3,4,2,5]))