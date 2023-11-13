# A list can contain anything! 

a_list = [2, 'Educative', 'A']

def foo():
    print("Hello from foo()!")

another_list = [a_list, 'Python', foo, ['yet another list']]

print(another_list[0]) # We expect this to output a_list
print(another_list[0][1]) # This will print "Educative"
print(another_list[1]) # Python
print(another_list[3]) # yet another list

another_list[2]()

# Important list functions
# 1. Append => Adds an element towards the end of the list: Takes constant time 0(1)
# list = [1, 3,5, "seven"]
# print(list)
# list.append(9)
# print(list)

# 2. Insert => Insert element to list. List insert(index, value); Works in 0(n)
list_insert = [1,3,5,'seven']
list_insert.insert(0, 2)
print(list_insert)

# 3. Remove => Removes the element at a given index:0(n)
list_remove = [1,3,5,'seven'] 
print(list_remove.remove("seven"))
print(list_remove.remove(3))

# 4. Pop => Remove element at a given index. If no index is given it removes the last element.
list_pop = [1,3,5,'seven']
print(list_pop.pop())
print(list_pop.pop(0))

# 5. Reverse => This function reverses the list
list_reverse = [1, 3,5,'seven']
list_reverse.reverse()
print(list_reverse)

# SLICING 
# list[start: end]
# Slice Notation Examples
# 1. Indexing Elements of a list

slicing_list = list(range(10))
print(slicing_list)# Output: 0,1,2,3,4,5,6,7,8,9
print(slicing_list[0: 4]) # Outputs: 0,1,2,3

"""
list[start:] : means all numbers greater than start uptill the range
list[:end] means all the numbers less than end uptill the range
list[:] means all numbers within the range
"""
print(slicing_list[3:])
print(slicing_list[:3])
print(slicing_list[:])

# Stepped indexing
# list[start: stop : step]
# Step specifies the increment in the list indices and can also be negative

step_list = list(range(10))
print(slicing_list[0:9:2])
print(slicing_list[9:0:-2])

# Example 3: Initializing list elements
x = list(range(5))
print(x) # 0,1,2,3,4
x[1:4] = [45,21,83]
print(x) # 0,45,21,83,4

# Example 4: Deleting elements from a list
del_list = list(range(10))
del del_list[::2]
print(del_list)

# Example 5: Negative Indexing
del_list[-2]

# Example 6: Slicing in strings
"""
We can also use slicing techniques on strings since strings are lists of charactes
"""
my_string = "somehow"
string1 = my_string[:4]
string2 = my_string[4:]
print(string1, string2)
