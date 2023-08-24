"""
Read more about list comprehensions here: https://stackoverflow.com/questions/68408065/understanding-the-syntax-of-list-comprehensions

Fun fact: Python is usually executed from right to left
"""
"""
Convert a list to a String using list comprehension
"""
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listTostr = ''.join([str(elem) for elem in s])
print(listTostr)

"""
Found this pretty interesting: Using map function 😎
"""
s2 = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
mapToStr = ''.join(map(str,s))
print(mapToStr)


