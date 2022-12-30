# Introduction to tuples

"""
Tuples => is an immutable sequence. Mostly used for record-keeping purpose.
"""

"""
Unpacking tuples.
"""

fruits = [('banana', 'yellow', 10), ('apple', 'red', 19)]

# Unpacking the tuple with a for loop
for name, color, _ in fruits:
    print(color)

# You can also unpack tuples using the * operator => Functionality is used when passing a tuple's values as parameters in a function.
def add(a,b):
    return a + b

numbers = (1,2)
result = add(*numbers)
print(result)

nested_tuple = (1,2,(4,5))
print(*nested_tuple)

lines = [(1, (2, 4), (1, 9)), (2, (-2, 4), (-1, 9)), (3, (-2, -4), (-1, -9))]
for ID, firstCords, secondsCords in lines:
    print('😁',firstCords)
    print(*lines)

'''
Challenge

The challenge involves a nested tuple of the line segments in the following format: (ID, (x1, y1), (x2, y2))

Here, ID is the unique number given to every line segment. 
Where x1 and y1 are the coordinates of one ending point, and x2 and y2 are coordinates of another ending point.

Implement the function filter_line_segments(lines), 
which finds all the line segments that only lie within the 2nd quadrant, and returns their IDs in a list.

In case, there are no line segments lying within the 2nd quadrant, return a string None.
'''

def filter_line_segments(lines):
    return [ID for ID, (x1, y1), (x2, y2) in lines if ((x1 != 0 or x2 != 0) and (y1 != 0 or y2 != 0) and (x1 <=0 and y1 >=0 and x2 <=0 and y2 >=0))]