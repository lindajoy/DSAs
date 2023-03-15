'''
Whats the input => An array of numbers
Whats the output => Returns an integer of how many times the array has been rotated


Finding the index less than the previous.
'''

def find_rotation(nums):

    for i in range(len(nums)):

        if nums[i] < nums[i - 1]:
            return i

    return 0


if __name__ == "__main__":
    print(find_rotation([2,3,4,5,1]))