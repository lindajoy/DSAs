# Chaining Comparisons

x = 15
print(id(x))
print(10 < x < 20)
# Should return True
print(10 < x and x < 20)
# Same as the condition above
x = 0
print(x)
print(id(x))

# Add more complex examples
x = 15
y = 25
print(10 < x < 20 < y < 30)
# Prints true.

# I think I get it now..
# Hmm You can compare lists.
print([1,2,3] == [1,2,3])

my_dict = {
    "name": "John",
    "age": 25
}

my_dict_2 = {
    "name": "John",
    "age": 25
}

print(my_dict  == my_dict_2)
