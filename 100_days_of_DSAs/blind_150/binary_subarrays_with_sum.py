"""
BINARY SUBARRAYS WITH SUM.

Given a Binary array nums and an integer goal, return the number of non-empty subarrays with sum goal.
A subarray is a contingous part of the array.
"""

# Did poorly in this question 😢

# Example 1:

# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4

# Explanation: The 4 subarrays are bolded and underlined below:
    # [1,0,1,0,1]
    # [1,0,1,0,1]
    # [1,0,1,0,1]
    # [1,0,1,0,1]

# Example 2

# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15

def numSubarraysWithSum(nums, goal):
    # Here we are creating a hashmap.
    # This represents that there is one subarray whose sum is 0.
    # Why are we starting with
    count = {0: 1}
    # This initializes a variable curr_sum to keep track of cumulative sum of elements encountered so far.
    curr_sum = 0
    # This initializes a variable total_subarrays to keep track of total count of subarrays whose sum is equal to the goal.
    total_subarrays = 0

    for num in nums:
        curr_sum += num
        print('Current Sum',curr_sum)
        if curr_sum - goal in count:
            print('Count:', count[curr_sum - goal])
            total_subarrays += count[curr_sum - goal]
            print(total_subarrays)
        count[curr_sum] = count.get(curr_sum, 0) + 1

    return total_subarrays

# print(numSubarraysWithSum([0,0,0,0,0], 0))
print(numSubarraysWithSum([1,0,1,0,1], 2))

# With this question, the time complexity is O(n)2 => (Quadratic solution)
def numSubarraywithSum2(nums, goal):
    count = 0
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum == goal:
                count += 1

    return count

print(numSubarraywithSum2([0,0,0,0,0], 0))
print(numSubarraywithSum2([1,0,1,0,1], 2))
