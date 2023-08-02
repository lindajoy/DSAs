"""
STRING OPERATORS
"""

# The + Operator => Concatenates strings
s = "foo"
t = "bar"
u = "baz"

print(s + t)
print(s + t + u)
print("Go team" + "!!!")

# The X operator => The multiplier operand n must be an integer.
# 🤯 It can be zero or a negative integer
s = "foo"
print(s * 4)
print('foo' * -8)

# The in operator => Membership operator that can be used with strings
# The in operator returns True if the first operand is contained within the second and false otherwise
print(s in "That\'s food for thought.")
print(s in 'That\'s good for now')

# The not in operator which does the opposite
print('Should return (True):', "z" not in "abc")
print('Should return (False):', "z" not in "xyz")

# BUILT IN STRING FUNCTIONS
"""
chr() => Converts an integer to a character
ord() => Converts a character to an integer
len() => Returns the length of a string
str() => Returns a string representation of an object
"""

a = ["Hello", "Joy"]
print(" ,".join(a))
print(ord("a")) # converts to number
print(chr(97)) # Converts back to character
stringOne = "I am a string."
print('Length of string One:',len(stringOne))

"""
str(obj) returns a string representation of an object
"""
k = 49.2
k = (str(k))
print(type(k))

'''
String Indexing: Individiual items in an ordered set of data can be accessed directly using numeric index or key value.
The process is referred to as indexing.
'''
stringTwo = "foobar"
print(stringTwo[0])
print(stringTwo[2])
print(stringTwo[len(stringTwo) - 1])

# Attempting to index beyond the end of the string results in an error
# 💣 Index out of range error.
# print(stringTwo[6])

"""
STRING SLICING
String indices are zero based. The first charcater in a string index has index 0.
This applies to both standard indexing and slicing.
"""
s = 'foobar'
print('Sliced Between 2:5:',s[2:5])
print('Sliced Before index 4:',s[:4])
print('Sliced from index 0 to 3:',s[0:4])
print('Sliced after the second index:', s[2:])
print('Sliced between the Seconde index and len(s):', s[2:len(s)])
print(s[:4] + s[4:])
print(s[:4] + s[4:] == s)

# 🤟🏼 💡 Slicing with  Negative Numbers

print(s[-5:-2])
print(s[1:4])
print(s[-5:-2] == s[1:4])

# Specifying a stride in a string slice
print('The slice starts with the first character and ends with the last character', s[0:6:2])
print('The slice starts with the second character at index 1(This is the second character)', s[1:6:2])

print('12345' * 5)
long_string = 'If Comrade Napoleon says it, it must be right.'
print(long_string[::-1])