"""
Minimum Number of Operations to Make Array Empty.

You are given a 0-indexed array nums consisting of positive integers.
There are two types of operations that you can apply on the array any number of times:
    * Choose two elements with equal values and delete them from the array.
    * Choose three elements with equal values and delete them from the array.

Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
"""
"""
Example I:
Input: 
Output: 4
"""
from collections import Counter


nums = [2,3,3,2,2,4,2,3,4]

def minOperations(nums):
    # Initialize an empty dictionary: To Store the occurence of each element.
    nums_count = {}
    # Initialize the number of count operations
    count = 0
 
    for i in nums:
        if i in nums_count:
            nums_count[i] += 1
        else: 
            nums_count[i] = 1

    print('Hello nums count', nums_count)
    for i in nums:
        if nums_count[i] >= 2:
            nums_count[i] -= 2
            count += 1
        if nums_count[i] >= 3:
            nums_count[i] -= 3
            count += 1
        else:
            count += 0
    if all(value == 0 for value in nums_count.values()):
        return count
    else:
        return -1


# print(minOperations(nums))
# print(minOperations([1, 2, 2, 2, 1, 3, 3, 3, 1]))
# print(minOperations([2, 2, 2, 1, 1, 1, 3, 3, 3]))
# print(minOperations([1,2,3,4,5]))

# 💡 Interesting Discovery instead of looping through the array and finding
# the number occurences, You can use the counter method
nums3 = [1, 2, 2, 2, 1, 3, 3, 3, 1]

count = Counter(nums3)
print(count)
# The base case of the solution is that :
# If the num_count = 1 then the shrinking of this element cannot happen so its -1
# if the num_count = 2 or 3 then the shrinking of the item can take place within one count.

# 💡 Makes sense?
# DFS Solution.
def minOperationsDynamic(nums):
    # create an empty dictionary
    cache = {}

    def dfs(n):
        if n < 0:
            return float("inf")
        if n in [2,3]:
            return 1
        if n in cache:
            return cache[n]
        
        res = min(dfs(n-2), dfs(n-3))
        print("Hello res", res)

        if res  == -1:
            return  -1
        cache[n] = res + 1
        return res + 1
    
    count = Counter(nums)
    print('Here is my count dictionary:',count)
    res = 0

    for n, c in count.items():
        print("Here is my n", n)
        print("Here is my c", c)

        op = dfs(c)
        if op == float("inf"):
            return -1
        res += op

    return res

print(minOperationsDynamic([4,4,4,4,4]))

random_example = 5

if random_example in [2,3]:
    print('Tunaingia Google')
    



