"""
Given two non empty integers, write a function that determines whether the second 
one is a subsequence of the first one.

A subsequence of an array is  a set of numbers that aren't necessarilingly adjacent in the array
but that appear in the same order as they appear in the array.

For instance, the numbers [1,3,4] are a subsequence of the array [1, 2, 3,4]
Example 2: [1, 2, 3, 4, 5], nums2 = [2, 4, 5]
"""

'''
Pseudocode:

'''

nums = [1,2,3,4,5,6,7]

# for i in range(len(nums)):
#     print('😁', i)

# for i in nums:
#     print('😊',i)

def findSubsequence(arry, subsequence):
    # Initialize left pointer
    leftPtr = 0

    # Loop the entire array
    for i in arry:      
        leftPtr += 1
        if(i == len(subsequence)):
            return True

    return False

      

nums2 = [1, 2, 3, 4, 5]
subs =  [2, 4, 5]

print(findSubsequence(nums2, subs))


