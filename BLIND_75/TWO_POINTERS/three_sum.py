"""
THREE SUM.

Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

nums = [-1,0,1,2,-1,-4]

"""
# Sorted nums:
# [-4, -1, -1, 0, 1, 2]
# Output: [[-1,-1,2],[-1,0,1]]

# Using Two pointers

def three_sum(arr):
    left = 0
    next_to_left = left + 1
    right = len(arr) - 1
    result = set()

    while left < right:
        if arr[left] + arr[next_to_left] + arr[right] == 0:
            result.add((arr[left], arr[next_to_left] , arr[right]) )
            left += 1
            next_to_left += 1
            right -= 1
        elif arr[left] + arr[next_to_left] + arr[right] < 0:
            left += 1
            next_to_left += 1
        elif arr[left] + arr[next_to_left] + arr[right] > 0:
            right += 1
    return list(result)

print(three_sum([-4, -1, -1, 0, 1, 2]))


