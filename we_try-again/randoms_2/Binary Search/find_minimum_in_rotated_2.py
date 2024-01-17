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


# 💡 Binary Search which takes O(log n) time

def findMinimumElementInArrayBinarySearch(nums):
    # Validate our input
    # Question for the interviewer:
    # Is it possible to recieve an array of length 0?
    if len(nums) == 0:
        return "My array is empty"
    
    if len(nums) == 1:
        return nums[0]

    # First we need to initialize my left and right pointer => This helps in calculation of the mid point
    left, right = 0, len(nums) - 1

    if nums[left] < nums[right]:
        return nums[left]
    
    while left <= right:
        mid = (left + right) // 2

        if nums[mid - 1] > nums[mid] < nums[mid +1]:
            return nums[mid]

        if nums[mid + 1] < nums[mid]:
            return nums[mid + 1]
        
        if nums[mid - 1] > nums[mid]:
            return nums[mid - 1]
        
        if nums[right] > nums[mid]:
            right = mid - 1
        else:
            left = mid + 2

print(findMinimumElementInArrayBinarySearch([3,1,2]))



