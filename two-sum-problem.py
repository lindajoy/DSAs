"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
Input: array, target

One question: is the array always going to be sorted?

Output are the indexes that add up to the target

Second question: How do we account for the case where there are no indices that add up to the 
                 target?

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Two pointers pattern: Traversing through the array and finding the sum between those two, Working with the assumption that the array
is sorted.

"""



class twoSumProblem():
    def twoSum(nums, target):
        nums = [(i, index) for index, i in enumerate(nums)]
        # Ooops never added the sort ---> 😶‍🌫️
        nums.sort()
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start][0] + nums[end][0] == target:
                return [nums[start][1],nums[end][1] ]
            elif nums[start][0] + nums[end][0] < target:
                start += 1
            else:
                end -= 1
            
        return None

        # nums = [(num, idx) for idx, num in enumerate(nums)]
        # print(nums)
        # nums.sort()
        # left = 0
        # right = len(nums) - 1
        # while left < right:
        #     if nums[left][0] + nums[right][0] == target:
        #         return [nums[left][1], nums[right][1]]
        #     elif nums[left][0] + nums[right][0] < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return None

if __name__ == "__main__":
    x = [3,3]
    y =  6
    print("Here are my results",twoSumProblem.twoSum(x,y))
    nums = [3,2,4]
    target = 6
    print("Here are my results",twoSumProblem.twoSum(nums,target))


# HashMaps (Value and index)