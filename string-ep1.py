'''
Implement an integer to string conversion function, and a string to integer conversison function,
For example, if the input to the first function is the integer 314,it should retum the string "31.4" and
if the input to the second function is the string "314" it should return the integer 314.

Hint: Build the result one digit at a time.

Notes: From this problem : I learned about the following methods in Python:
       ord() => Takes a string argument of unicode character and returns its integer
       char() => Takes an integer argument and returns the string representing a character at that code point
'''

# S') + ''.join(reversed(s))



# def string_to_int(s):
#     return functools.reduce(
#         lambda running_sum , c: running_sum * 10 + string. digits. index (c),
#          s[s[0] == '-' :],0) ^ (-1 if s[0] == '-' else 1)

# print(int_to_string(234))
# print(string_to_int('abc'))


RED, WHITE, BLUE = range(3)
print("Blue:", BLUE)
print("Red:", RED)
print("White:", WHITE)

x= "sasa"

print(x[::-1])