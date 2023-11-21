"""
Given an unsorted list A
, the maximum sum sub list is the sub list (contiguous elements) from A
for which the sum of the elements is maximum. 
In this challenge,
 we want to find the sum of the maximum sum sub list. This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.
"""

# SLOW DOWN, BREATHE 😮‍💨

x = [-4,2,-5,1,2,3,6,-5,1]

# if not x:
#     print("I am a list without anything!")

def find_max_sublist(x):
    if not x:
        return 0
    if len(x) == 1:
        return x[0]
    # Initialize the max values.
    _max = _gmax = x[0]
    for el in x[1:]:
        if _max < 0:
            _max = el
        else:
            _max += el
       
    return _gmax

print(find_max_sublist(x))
print(find_max_sublist([-2,-3,-4, -5,-1, -6]))
print(find_max_sublist([1,-3,4,-2,-1, 6]))