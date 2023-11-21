# Reminding myself of some string operations => Strings are also iterables in python
# Meaning that you can loop over them, Slice them , reverse them.
# Here are a few examples:
my_string = "Good things are coming!"

# loops over the string
for i in my_string:
    print(i)

my_sliced_string = my_string[0 : 5]
print(my_sliced_string)

# Wait a minute, what does the split method do? 
# 💡 Huh 😄 Converts it to a list hehe!
split_string = my_string.split()
print("Split string:", split_string)


# Did you know you can sort a string?
# ❎ TIP 💡‼️‼️🌍
# Hmm, if your string has both uppercase and lower case always ensure that you have converted it to lowercase
basic_string = "helloworld"
mixed_string = "HELLOworld"
#If you do, ''.join(sorted(basic_string)) you will get: EHLLOdlorw; which is ideally not what we want.
mixed_string_sorted = ''.join(sorted(mixed_string.lower()))
print("Sorted Mixed String", mixed_string_sorted)
sorted_string = ''.join(sorted(basic_string))
print("Sorting a string:", sorted_string)


# Lets remove the spaces in my string
my_unspaced_string = ''.join(my_string.split())
print('Unspaced string:', my_unspaced_string)

# OR
my_unspaced_string_2 = my_string.replace(" ", "")
print('Tried replace method instead to remove spaces:', my_unspaced_string_2)

# What does strip method on strings do in Python?
my_sample_string = "  a line with leading and trailing space  "
print('My stripped sentence:', my_sample_string.strip())

# There is also rStrip and Lstrip()
strip_string = "  Joy is Learning about string manipulation  "
# ==> Stripping from the end
print('End stripping: ', strip_string.rstrip())
# ===> Stripping from the start
print('Left Stripping: ', strip_string.lstrip())

# Did you know that The first interview you did at Google was a string question?
# You did not do so well...😕
# Oh well, But you can decide what will happen in your next google interview..
# Here was the question:

"""
Given a string: add(10, 4) or add(3,4), Return the total sum of the string

💡 If i remember correctly the interviewer said that we can assume that the
   input string will always be an add function.

Questions for the interviewer:
    1. Should we assume that our numbers will either be single or double digit ie Do we ever expect a three digit number?
       Say add(100, 4000)
    2. Just to clarify, The string in this case will always be add right? 
    3. Am I allowed to manipulate the string? 

Okay, lets break it down:
    INPUT: String
    OUTPUT: Number

Pseudocode: Here's what I am thinking:
1.  A string is an iterable in python right? We can remove the first 4 characters having in mind that this will always be an
    additional operation. And we can remove the last ")"
2.  So that means by now we will have or our string will be "10,4"
3.  We can decide to split the reminder of the string to give us ['10', '4']
4.  Next, we will loop through the list converting each string to a number and doing the addition.
""" 

input_str = "add(10,4)"
input_str_2 = "add(100,4000)"

def addUsingString(str):
    sliced_str = str[4: -1]
    sliced_str = sliced_str.split(',')
    total_sum = sum(int(num) for num in sliced_str)
    return total_sum

print(addUsingString(input_str))
print(addUsingString(input_str_2))

"""
Show your long term thinking skills: I dont like it when we mutate a specific variable alot of times it can get messy!
"""

# 💡 Another method would be:
def calculate_add(str):
    input_string = str.replace('add(', ""). replace(")", "")
    print(input_string)

    # You can change it to a list
    input_list = input_string.split(',')
    totalSum = sum(int(num) for num in input_list)
    return totalSum

    # Or 
    # numbers = input_str.split('')
    # totalSum = sum(int(num.strip()) for num in input_list)
    # return totalSum



print(calculate_add(input_str))
