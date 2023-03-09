'''
You are playing a game involving a circular array of non-zero integers nums. 
Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, 
and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1

'''


def circular_array_loop(nums):

    current_direction = None

    for i in range(len(nums)):

        if abs(nums[i] == len(nums)):
            continue

        if nums[i] >= 0:
            current_direction = True
        else:
            current_direction = False

        slow_ptr = i
        fast_ptr = i

        # we cant find the loop for that number when any pointer equals to -1
        while slow_ptr != fast_ptr or slow_ptr != -1 or fast_ptr != -1:
            # Move slow pointer one step and fast pointer two steps forward/backward
            slow_ptr = next_step(nums, slow_ptr, current_direction)
            
            if slow_ptr == -1:
                break
            fast_ptr = next_step(nums, fast_ptr, current_direction)

            if (fast_ptr != -1):
                fast_ptr = next_step(nums, fast_ptr, current_direction)

            if fast_ptr == -1 or slow_ptr == fast_ptr:
                break

        if slow_ptr == fast_ptr and slow_ptr != -1:
            return True

        return False

def next_step(nums, current_index, current_direction):

    next_direction = None

    if nums[current_index] >= 0:
        next_direction = True
    else:
        next_direction = False

    # Loop can't be found if the loop direction is changed
    # or the value of the array element is equal to the length of the array
    if (next_direction != current_direction or abs(nums[current_index] % len(nums)) == 0):
        return -1
    find_step = current_index + nums[current_index]
    find_step = find_step % len(nums)

    return find_step


x = [1,3, -2, 4, 1]
print(circular_array_loop(x))
