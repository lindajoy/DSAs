"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Link: https://leetcode.com/problems/first-bad-version/

"""

'''
Typical Binary Search Problem

# Start with the middle element:
# If the target value is equal to the middle element of the array, then return the index of the middle element.
# If not, then compare the middle element with the target value,
# If the target value is greater than the number in the middle index, then pick the elements to the right of the middle index, and start with Step 1.
# If the target value is less than the number in the middle index, then pick the elements to the left of the middle index, and start with Step 1.
# When a match is found, return the index of the element matched.
# If no match is found, then return -1
'''

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Initialize the start and the end value
        start, end  = 1, n

        while start <= end:
            mid = start + (end-start) / 2
            if isBadVersion(mid):
                start = mid
            else:
                left = mid + 1

        return left

    

# my_list = list(8)
# print(my_list)
print(7//2)