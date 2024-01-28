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

print('Using is operator:', 'Hello' is 'Hello')

a = [1, 2, 3]
# 💡 Returns True if the two memory points => point to the same memory location.
b = a
print(b is a)  # True
print(b == a)  # True

c = [1, 2, 3]
print(c is a)  # False
print(c == a)  # True

# b and a are two variables that point to the same object in memory, so b is a returns True. 
# The == operator also returns True because the values of a and b are the same.
# Always try to use the == sign.