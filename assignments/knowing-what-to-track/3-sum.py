"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(nums):
    eNums = [ (i, index) for (i, index) in enumerate(nums)]
    eNums2 = sorted(eNums, key=lambda x: x[1])
    print(eNums2)

    # Initialize the left Pointer
    leftPtr = 0
    leftOnePtr = leftPtr + 1
    rightPtr = len(nums) - 1
    endArray = []


    while leftPtr < rightPtr and leftOnePtr < rightPtr:
        if eNums2[leftPtr][1] + eNums2[leftOnePtr][1] + eNums2[rightPtr][1] == 0:
            print(eNums2[leftPtr][1] , eNums2[leftOnePtr][1] , eNums2[rightPtr][1])
            result = [ eNums2[leftPtr][1], eNums2[leftOnePtr][1], eNums2[rightPtr][1] ]
            endArray.append(result)
            leftPtr += 1
            leftOnePtr = leftPtr + 1

        elif eNums2[leftPtr][1] + eNums2[leftOnePtr][1] + eNums2[rightPtr][1] < 0:
            print(eNums2[leftPtr][1] + eNums2[leftOnePtr][1] + eNums2[rightPtr][1])


            leftPtr += 1
            leftOnePtr = leftPtr + 1

        elif eNums2[leftPtr][1] + eNums2[leftOnePtr][1] + eNums2[rightPtr][1] > 0:

            rightPtr = rightPtr - 1

    return endArray







x = [-1,0,1,2,-1,-4]
y = [0,1,1]
z = [0,0,0]
print(threeSum(x))
print(threeSum(y))
print(threeSum(z))


lis1 = [(5, -4), (0, -1), (4, -1), (1, 0), (2, 1), (3, 2)]
lis1.sort(key=lambda i : i[1])

print