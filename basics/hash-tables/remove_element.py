"""
REMOVE ELEMENT

Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

# What the question is asking above is what will be the length of the array if i remove all the ks from my array.

def remove_element(arr, k):
    n = len(arr)
    i = 0

    # Loop through the array
    while i < n:
        # Check whether the value at the specific index is equal to the target
        if arr[i] == k:
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            n -= 1  # decrement the length of the array by discarding the last element
        else:
            i += 1
    # Return length n at the end
    return n

print(remove_element([3,2,2,3], 3))
print(remove_element([0,1,2,2,3,0,4,2],2))