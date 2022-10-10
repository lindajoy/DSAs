"""
Selection Sort

Pseudocode:
      i) Find the smallest element in the array.
      ii) Insert/ swap with the element in the first position.
      iii) Repeat untill the entire array is sorted.
"""
# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    pos_to_insert = 0
    while pos_to_insert < len(array):
        smallest = pos_to_insert

        # find smallest
        for idx in range(pos_to_insert + 1, len(array)):
            if array[idx] < array[smallest]:
                smallest = idx

        # swap
        array[pos_to_insert], array[smallest] = array[smallest], array[pos_to_insert]

        pos_to_insert += 1

    return array

post_array = [7,1]
print(selectionSort(post_array))


"""
Divide the input array into two subarrays in place. 
The first subarray should be sorted at all times and should start with a length of 0, while the second subarray should be unsorted.
Find the smallest (or largest) element in the unsorted subarray and insert it into the sorted subarray with a swap.
Repeat this process of finding the smallest (or largest) element in the unsorted subarray and
 inserting it in its correct position in the sorted subarray with a swap until the entire array is sorted.
"""

# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space


def selectionSort00(array):

    # select the smallest element and place it at i
    for i in range(len(array) - 1):

        smallest = i
        for idx in range(i+1, len(array)):
            if array[smallest] > array[idx]:
                smallest = idx

        # swap
        array[i], array[smallest] = array[smallest], array[i]

    return array


post_array = [7,1]
print(selectionSort00(post_array))

'''
💡 Ideas learnt from this implementation
'''
'''
   Swaping 

   Python evaluates expressions from left to right. Notice that  when evaluating an assignment,
   the right hand side is evaluated before the left hand side.

   See Docs: https://docs.python.org/3/reference/expressions.html#evaluation-order

   This means for the following expression a,b = b,a

   The right hand sde b, a is evaluated, that is to say, a tuple of two elements is
   createed in the memory. The two elements are the objects designated by the identifiers b and a,
   that were existing before the instruction is encountered during the execution of the program.

   Just after the  creation of this tuple, no assignment of this tuple object has still been made,
   but it doesn't matter, Python internally know where it is.

   Then, the left hand side is evaluated, that is to say, the tuple is assigned to the left side.

   As the left hand side is composed of two identifiers, the tuple is unpacked in order that the first ideni=fier a
   be assigned to the first element of the tuple (which is the object b before the swap because it had name b)
   and the second identifier b is assigned to the second element of the tuple.

   For more info: https://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python#:~:text=Tuple%20swap&text=Is%20the%20simplest%20and%20the%20only%20one%20that%20is%20not%20obfuscated.
'''

x = 60
y = 70
x, y = y, x

print('The swapped value of x:', x)
print('The swapped value of y:', y)