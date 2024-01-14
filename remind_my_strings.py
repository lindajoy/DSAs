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

# 💡 str.format and f-strings: Format values in a string
# Given the following variables:
i = 10
f = 1.5
s = "foo"
l = ['a', 1, 2]
d = {'a': 1, 2: 'foo'}

# The following statements are all equivalent:
print(str.format('{} {} {} {}', i, f, s, l, d))
print('I am from {}. I like bananas from {}!'.format("Embu", "Embu"))
print('My favorite movie is {0}'. format('Zootopia'))
print('My name is {0} and I work at {1}, You can call me a {2}!🤔'.format('Joy', 'Google', 'Noogler'))
  
# 💡 STRIPPING UNWANTED LEADING/TRAILING CHARACTERS FROM A STRING
# str.strip removes any leading or trailing characters contained the arguments
print('   On a Sunday morning, I prefer going to church to coding  '.strip())

# str.rstrip starts from the end of the string while str.lstrip splits from the start of the string
print('   On a Sunday morning, I prefer going to church to coding  '.rstrip())
print('   On a Sunday morning, I prefer going to church to coding  '.lstrip())

#💡 Reversing a string
# Note that the output here is: ariwaW hadiL yoJ
print('My name reversed:',''.join(reversed(my_name)))
print('A random string reversed',''.join(reversed('joy')))

# What about sorting? 💡
# for this expect the output:  a a a d h i i j l o r w w y
print('My name sorted:',' '.join(sorted(my_name.lower())))

# Hehe fun fact, 
# When you sort without converting to lower case: The capital letters come first.
# For this expect the output: J L W a a a d h i i o r w y
print('My name sorted:',' '.join(sorted(my_name)))


