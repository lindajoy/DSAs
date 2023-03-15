# Adding elements in an array

a = [1,2,3]
b = [8,9,0]

print(b + a)

nums = [1,2,3,4,5,6,7]
end = len(nums) - 1
x = nums[end-3: end + 1]
print('This is x', x)
print(nums[0: end-3])


"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""

def Solution(nums, k):
   endIndex = len(nums) - 1
   els = k - 1

   elementsToRemove = nums[endIndex-els : endIndex + 1]
   #slice the array
   nums = nums[0: endIndex - (k+1)]

   return elementsToRemove + nums

X = [1,2,3,4,5,6,7]
K = 3

print(Solution(X,K))


def SolutionTwo(nums, k):

    for i in range(len(nums)):
        (i + k) % len(nums)
        return nums

print(SolutionTwo(X,K))


list3 = [1,2,3,5]

for i in enumerate(list3):
    print(i)

print('boom',[i for i in enumerate(list3)])