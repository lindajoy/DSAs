"""
Bubble sort
   Pseudocode:
    i) Compare the first element with the second element
    ii) If the first element is greater than the the second element then move and compare with the second
    iii) Repeat with the third till the list is fully sorted.
"""
# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):

    did_swap = False
    while True:
        did_swap = False

        for idx in range(1, len(array)):
            if array[idx] < array[idx-1]:
                # swap
                array[idx],  array[idx-1] = array[idx-1], array[idx]
                did_swap = True

        if not did_swap:
            return array

array_2 = [2,7,6,5,1,3]
print(bubbleSort(array_2))

"""
Bubble sort solution 2
"""
def bubbleSort00(array):
    if len(array) < 2:
        return array

    is_sorted = False
    while not is_sorted:
        is_sorted = True

        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                is_sorted = False
                # swap
                array[i], array[i+1] = array[i+1], array[i]

    return array

post_array = [7,1]
print(bubbleSort00(post_array))

'''
not operator - (Negation)
 
The task of the not operator is to reverse the ruth value of its operand

not True => False
not False => True

Not Operator:
        i) Checking unmet conditions in the context of if statements and while loops
        ii) Inverting the truth value of an object or expression
        iii) Checking if a value is not in a given container
        iv) Checking for an objects identity

💡 Fun Fact : Python evaluates math and comparison operators first, Then  evaluates logical operators!

'''

print (not True == False) # Returns True
print (False == not True) # Invalid syntax
print ( False == (not True))  # Returns True