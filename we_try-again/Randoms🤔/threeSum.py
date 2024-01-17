"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]] 

Another Example (That failed on my first solution):

Input: nums = [-2,0,1,1,2]
Output: [[-2,0,2], [-2,1,1]]

"""

def threeSum(nums):
    target = 0
    unique_triplets = set()
    nums.sort()

    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total_sum = nums[i] + nums[j] + nums[k]
            if total_sum == target:
                unique_triplets.add((nums[i] , nums[j] , nums[k]))
                j += 1
                k -= 1
            elif total_sum > target:
                k-=1
            else:
                j+=1
    return list(unique_triplets)
    
print(threeSum([-1,0,1,2,-1,-4]))

