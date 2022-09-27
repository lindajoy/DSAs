# Arrays are provided by the list type. The tuple is very similar to the list type with the constraint that its immmutable.
# basic operations in the list

 
# 1. Lists may contain different types but usually all items have the same type
import re


a = [1,2,3,4,5,'hello']
print(a)

# 2. Lists contain the same type
b = [1,2,3,4,5]
print(b)

# 3. Appending
b.append(6)
print("Appended B:", b)

# 4. Extending => Extends another list by adding another existing enumerable i.e list
b.extend(a)
print("Extended B:", b)

# 5. Index() => Returns the index of the first occurence of the integer when found
c = b.index(3)
print("Here's the index of 3:", c)

# 6. Insert(value, index) => Inserts a value at a particular index.
b.insert(1,4)
print("Here's array_d:", b)

# 7. pop(index)
b.pop(1)
print("Popped the value at index 1:", b)

# 8. remove(value)
b.remove(4)
print("Removed element of value 4:", b)

# 9. reverse - Reverses the list
b.reverse()
print("Here's the reversed list:", b)

# 10. sorts the array
b.pop(0)
b.sort()
print("Here's the sorted list", b)

# 11. You can also reverse the list using the sort method
print('Wewe:',b)
b.sort(reverse=True)
print("Reversed again:",b)

#Instantiating a 2D array using a list
two_dimensional = [[1,2,3], [4,5,6],[7,8,9]]

#accessing the first array
print(two_dimensional[0])

#accessing the first element in the first array
print(two_dimensional[0][1])

#insert
print(two_dimensional.insert())
