nums = [3, 4, 5, 1, 2]
nums2 = [4,5,6,7,0,1,2]
nums3 = [11,13,15,17]

# This is the Brute force approach:
# The time complexity will be 0(n) => N indicating the length of the array.

def findMinimumElementInArray(nums):
    # Remove the edge cases

    if len(nums) == 1:
        return nums[0]
    
    if len(nums) == 0:
        return "Array is Empty!"
    
    if nums[0] < nums[len(nums)- 1]:
        return nums[0]

    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return nums[i+1]
        
print(findMinimumElementInArray(nums3))


