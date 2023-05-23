dict_one = { 7:[5,2],6:[2,4],10:[4,6],9:[6,3],4:[3,1] }
[5,2,4,6,3,1]
maxInDict = max(dict_one)
print(dict_one[maxInDict])

def maxSubarray(nums):
    left = 0
    right = left + 1
    dict_two = {}

    while right < len(nums):
        sum = nums[left] + nums[right]
        dict_two[sum] = [nums[left], nums[right]]
        left += 1
        right += 1
    
    maximum_val = max(dict_two)
    return dict_two[maximum_val]

print(maxSubarray([5,2,4,6,3,1]))



