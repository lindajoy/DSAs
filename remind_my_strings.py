# How de we sort a string?
str = 'helloworld'
# This is how we sort a string
sorted_str = ''.join(sorted(str))
print(sorted_str)

# How do we slice a string?
print(sorted_str[1:-1])
print('From index 1 to the end 1', sorted_str[1:])

random_str = "add(3,4)"
print('Let me slice this thing up:',random_str[4:-1])
sliced_str_operation = random_str[4:-1]
sliced_list = sliced_str_operation.split(',')

count = 0
for i in sliced_list:
    count += int(i)

print("My count", count)

# That was an easy question to fail at. 🤔

# SOME STRING METHODS.
# i) Changing the capitalization of a string.
my_name = "Joy Lidah Wawira"
print(my_name.casefold())
# converts to lower case equivalent
print('My name in lower case', my_name.lower())
# takes every character and converts it to its uppercase equivalent
print('My name in upper case', my_name.upper())
# returns a capitalizied version of the first character and lowercase all others
print('My name capitalized',my_name.capitalize())
#  title returns the title cased version of the string, every letter in the beginning of a word is made an upper case.
print('this is a `string`'.title())
# swapcase returns a new string object in which all lower case characters are swapped to upper case characters and all upper case characters to lower
'this is A STRING'.swapcase()


  