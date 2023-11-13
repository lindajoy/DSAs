"""
An array is just an ordered sequence of homogenous elements.
An array can hold elemensts of one type
"""
import array
# Type defines the data type of the array and list is a python list containing homogenous elements
new_array = array.array('type', [list])

#type: 'f' (float), initializer list;[1,2,3]
# Here f indicates the array is of type float.
print(new_array[0])
initializer_list =[2,5,43,5,10,52,29,5]
number_array = array.array("i", initializer_list)

# Array slicing is done exactly the same way list slicing is done
print(number_array[1:5]) # 2nd to 5th
print(number_array[:-5]) # beginning to 3rd
print(number_array[5:]) # 6th to end
print(number_array[:]) # beginning to end

# CHANGING OR ADDING ARRAY ELEMENTS
# This changes the value to [0,5,43,5,10,52,29,5]
number_array[0] = 0

# changing the third to the 5th element
number_array[2:5] = array.array("i", [4,6,8])
print(number_array)