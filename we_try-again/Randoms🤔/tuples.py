# Tuples are values separated by commas.

t = 12345, 54321, 'hello'
print(t)
print(t[0])

# Tuples may be nested.
u = t, (1,2,3,4,5,6)
print(u)

# Tuples are imuttable
# t[0] = 88888
# print(t)

v = ([1,2,3], [3,2,1])
v[0][1] = 5
print(v)

# Creating an empty tuple => Empty tuples are constructed by an empty pair of parentheses.
# A tuple with one item is constructed by following a value with a comma.
empty = ()
singleton = 'hello', # <-- note trailing comma
print('Length of my empty Set:', len(empty))
print('Length of my set with one element:', len(singleton))

# The statement t = 12345, 54321, 'hello!' is an example of tuple packing.
t = 12345, 54321, 'hello!'

# The reverse operation is also possible.
x, y, z = t
print(x)
print(y)
print(z)

# Hmm let me try something with sets:
basket = {'apple', 'mango', 'apple'}
print(basket)
new_list = list(dict.fromkeys(basket).keys())
print('My new list:', new_list)
x1, y1 = basket
print('Apple:', x1)
print('Mango:', y1)

