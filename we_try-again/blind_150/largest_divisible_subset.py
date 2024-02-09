"""
💡 LARGEST DIVISIBLE SUBSET

Given a set of distinct positive integers nums, return the largest subset answer such that 
every pair (answer[i], answer[j]) of elements in this subset satisfies:
        answer[i] % answer[j] == 0, or
        answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Input: [1,2,3]
Output: [1,2] or [1,3]

Input: [1, 2, 4, 8]
Output: [1, 2, 4, 8]
"""
# This is a Dynamic Programming Question

# Question for the interviewer?
# 1. A pair does not have to be contingous right? 
# 2. Can we assume if our array has 1, we can match it with any other pair? 🤔

# 💡 Memoization Optimization
# Takes in an array and we need to return an array list of integers.

def largestDivisibleSubset(nums):
    # Sort the array
    nums.sort()
    cache = {}

    # ex = [1,2,5,15,45]
    def dfs(i, prev):
        if i == len(nums):
            return []
        if (i, prev) in cache:
            return cache([i, prev])
        
        res = dfs(i + 1, prev)
        if nums[i] % prev == 0:
            tmp = [nums[i] + dfs(i + 1, nums[i])]# include nums[i]
            res = tmp if len(tmp) > len(res) else res

        cache[(i, prev)] = res
        return res
    
    return dfs(0,1)





    return dfs(0,1)

