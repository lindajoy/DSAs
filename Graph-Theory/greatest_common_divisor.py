"""
GREATEST COMMON DIVISOR TRAVERSAL

You are given a 0-indexed integer array nums, 
and you are allowed to traverse between its indices. 
You can traverse between index i and index j, i != j, 
if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, 
where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, 
or false otherwise.

"""
# Whats the input: An array
# Whats the output: A boolean if its possible to traverse between all such pairs of indices

# Union Find 🥶 🫣

abs_k = [1,2,3,4,5]
print([i* 2 for i in abs_k])

