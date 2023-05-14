"""
Converting a list to a string in Python
"""

x = ['h','e', 'l','l']

c = ''.join(x)
d = str(x)
# print(c)
print(d)

"""
🤩 Remove duplicates from a list using set method
"""

restraunts = ["KFC", "ChickenInn", "CooperIvy", 'Sankara', 'Sankara', "kfc"]

print(list(set(restraunts)))

"""
Sorting a string
"""

some_string = "happy"
some_string_2 = ''.join(sorted(some_string))
print(some_string_2)


"""
Enumerating using list comprehensions
"""

some_list = ["Firefly Lane", "Harry Potter", "A star is born", "Lord of Rings"]

enumerate_list = [(i, num) for i, num in enumerate(some_list)]

enumerate_list.sort(key=lambda x: x[1])

print(enumerate_list)

"""
🎲 Looping through a dictionary
"""

d = {"a": 1, "b": 2, "c": 3, "d": 3}

print(list(set(d.values())))
print(list(d.keys()))

"""
Variables in Python are mainly of 2 types:

Global variables: Declared outside the function or in a global scope.
Local variables: Declared inside the function’s body or in a local scope.

Non-Local Keyword Python => is used to work with variables inside nested functions whose local scopes are not defined.
"""

# First Function
def f():
    x = 10
    
    # Nested Function
    def g():
        nonlocal x
        x = 1
    g()
    print (x)
    
print(f())
