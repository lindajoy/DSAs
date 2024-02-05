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
# Whats the input? An array.
# Whats the output? The number of entries in our array.

# Time Complexity is: O(N)
# Space Complexity is : O(1)

# Using Pop
def deleted_duplicates(nums):
    if not nums:
        return []
    
    left = 0
    right = left + 1

    while right < len(nums):
        if nums[left] == nums[right]:
            # Proud of you => used pop; Takes in an index.
            # Can we use remove?
            # Yes we can!
            nums.pop(left)
        left += 1
        right += 1
    return len(nums)

print(deleted_duplicates([2,3,5,5,7,11,11,13]))

# Using remove
def deleted_duplicates2(nums):
    if not nums:
        return []
    
    left = 0
    right = left + 1

    while right < len(nums):
        if nums[left] == nums[right]:
            # Proud of you => used pop; Takes in an index.
            # Can we use remove?
            # Yes we can!
            nums.remove(nums[left])
        left += 1
        right += 1
    return len(nums)

print(deleted_duplicates2([2,3,5,5,7,11,11,13]))

random_str = "add(10,40)"
list_generated = random_str[4:-1].split(',')
summing_up = 0
for i  in list_generated:
    summing_up += int(i)

print(summing_up)

def summing_given_string(str):
    split_str = str[4:-1]
    list_str = split_str.split(',')
    total_sum = 0

    for i in list_str:
        total_sum += int(i)
    return total_sum

print(summing_given_string(random_str))

