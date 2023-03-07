"""
EDUCATIVE TOPIC ONE: SUBTOPIC THREE SUM OF THREE NUMBERS

Given an array of integers, nums, and an integer value, target,
determine if there are any three integers in nums whose sum equals the target. 
Return TRUE if three such integers are found in the array. Otherwise, return FALSE.
"""

def sumofThreeNumbers(nums, target) -> bool:
    # Sorting numbers in the array
    nums.sort()

    # Loop through the entire array
    for i in range(0, len(nums)- 2):
        # Set the indexes of the two pointers
        # Index of the first of the remaining elements
        low = i + 1
        high = len(nums) - 1

        while low < high:
            #check if sum of the triple is equal to the sum
            triple_sum = nums[i] + nums[low] + nums[high]

            if triple_sum == target:
                return True
            elif triple_sum < target:
                low += 1
            else:
                high -= 1
        return False
