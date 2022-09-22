# String Operations -> Common opertions in strings

name_1 = "Varun"
print(id(name_1))

name_1 = "Tarun"
print(id(name_1))

# This wont work because strings are immutable
# name_1[0] = "F"

print(name_1)

my_string = "Hello World"
print(id(my_string))
my_string = "Hello"
print(id(my_string))


print(my_string + my_string)


# Iterating through a string
count = 0
for letter in my_string:
    if(letter == 'l'):
        count += 1

print('Letters found', count)


# string membership
print('l' in my_string)
print('l' not in my_string)

# Enumerate function
enumerate_string = "colder"
print(list(enumerate(my_string)))
print(len(my_string))
print(my_string[1:3])

my_string_2 , random_no = "hello", 2
print(my_string_2)
print(random_no)