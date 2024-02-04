# DELETE DUPLICATES FROM A SORTED ARRAY => Elements of Programming.

"""
This problem is concemed with deleting repeated elements from a sorted array. 
For example, for the array [2,3,5,5,7,11,11,13], then after deletion, 
the array is [2,3,5,5,7,11,11,13]. After deleting repeated elements, there are 6 valid entries. 
There are no requirements as to the values stored beyond the last valid element.
Write a program which takes as input a sorted array and updates it so that all duplicates have been removed
and the remaining elements have been shifted left to fill the emptied indices.
Return the number of valid elements.
Many languages have library functions for performing this operation- you cannot use these functions.

"""

# Time Complexity is: O(N)
# Space Complexity is : O(1)

def deleted_duplicates(nums):
    if not nums:
        return []
    
    left = 0
    right = left + 1

    while right < len(nums):
        if nums[left] == nums[right]:
            nums.pop(left)
        left += 1
        right += 1
    return nums

print(deleted_duplicates([2,3,5,5,7,11,11,13]))