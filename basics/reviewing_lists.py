# LIST

a = [1,2,3,4,5]
b = [6,7,8,9]

print('Concatenation:', a + b)
print('Extending:', a.extend(b))
c = a + b
# Finding the index of a specific element
print(c.index(1))

nums1 = [1, 2, 3, 4, 5, 6, 7, 7]
nums2 = [8, 9, 10]
# Extend list by appending all elements from b
print(nums1.extend(nums2))

# Using pop: Removes and returns the item at index.
print(nums1.pop(2))
# Removes the element at index 0
print(nums2.pop(0))
# Removes the last element
print(nums1.pop())

# Removes the first occurence of the specified value.
print(nums1.remove(4))
print(nums2.remove(10))
print(nums1.reverse())

# Accesing values in a list
lst = [1,2,3,4]
print(lst[0])
print(lst[1])
print(lst[-4])
print(lst[1:])
print(lst[2:])