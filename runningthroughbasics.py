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