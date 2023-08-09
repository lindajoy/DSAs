"""
Python List Operations
"""

# Creating an empty list.
empty_list = []

# Mutable Operations => You can change the structure of the array.

# Append operation => Adds an element to a list.
x = [1,2]
x.append('h')
print('Adds h to the end of the list',x)

# Extend operations => Adds another list to the end of a list
y = [1,2]
y.extend([3,4])
print('Extends a list to another list:', y)

# Insert operation => Inserts an element to a specific position in the list.
insert_to_list = ['a', 'b']
insert_to_list.insert(0, 'y')
print('Inserted y to my list',insert_to_list)

# Delete operation => Deletes an element in the specific index
delete_on_list = [1, 2, 3]
del delete_on_list[1]
print('Deleted an element on the list:', delete_on_list)

# Remove the first match for the specified item
x = [1,2,3, 'h', 6, 'h']
x.remove('h')
print('Removed the first h on my list',x)

# Reverse => Reverses the order of the elements in the list, this places the final elements in the begining
# and the initial elements at the end
reverse_list = [1,2,'h',3, 'h']
reverse_list.reverse()
print(reverse_list)

# Sort => This method sorts the elements of the list from the smallest to largest.
# This method can be modified by using the parameter reverse = True
sort_array = [3,2,1,4]
sort_array.sort()
print(sort_array)

y = ["R", "C", "Python", "Java", "r"]
y.sort(reverse=True)
print("Reversed array:",y)