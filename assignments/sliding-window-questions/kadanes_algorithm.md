## Kadane's Algorithm

### First let's understand what Dynamic Programming Is.
Dynamic programming is a method for solving a complex by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solution using a memory based data structure.

Dynamic programming is more like remembering stuff somewhere so we can use it later.
(https://www.quora.com/How-should-I-explain-dynamic-programming-to-a-4-year-old/answer/Jonathan-Paulson)

So the next time  the same sub-problem occurs, instead of recomputing its solution, one simply looks up previously computed solution, thereby saving computation time.

Using the question: https://leetcode.com/problems/maximum-subarray/description/

#### How would we solve it using Brute Force?
```
# Brute Force Approach
# Time Complexity: Quadratic (O(n))
# We have Two for loops

def maximumSubarray(nums):
   max_sum = float('-inf')
   n = len(nums)

   for i in range(n):
    for j in range(i, n):
        # Calculate the sum of the subarray
        subarray_sum = sum(nums[i:j+1])
        max_sum = max(max_sum, subarray_sum)

   return max_sum
```

Kadane's algorithm Formula: localMaxSum[i] = max(input[i], input[i] + localMaxSum[i-1])
