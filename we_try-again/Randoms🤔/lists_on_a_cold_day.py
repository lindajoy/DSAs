# 💡 Lists 💡
# 👻 Fun fact modifying b also modifies a = Hence this is not a good a copying mechanism

a = [1, 2 ,3, 4, 5, 6]
b = a
print("Hello b:", b)
b.append("Added some element")
print("Modified b:", b)
print("Has it affected a?", a)

# If you want to copy a list effeciently this is what you can do
# So to copy You can use the slice method or the list(method)
names = ['Justin', 'Mwenda', 'Ann', 'Mukami', 'Joy', 'Lidah']
new_names = names[:]
new_names.append('Fox')
print('Here are my new names', new_names)
new_new_names = list(names)
new_new_names.append("Wawira")
print('Here are my new new names', new_new_names)

# 💡 Remove function => Remove first occurence of element from list.
new_new_names.remove('Wawira')
print("Did i remove 'Wawira'?", new_new_names)

# If value does not exist python, returns a valueexpection error!

# Insert, takes in index where you want to insert and the element you want to insert.
new_names.insert(0,'Ann')
print('😮‍💨 Added Ann at index at index 0:',new_names)

# Index: Returns the first index of an element.
print('Should expect 0:', new_names.index('Ann'))
# Index => can also take in index to start (Startindex) when looking for an element
print("Should expect 3:", new_names.index("Ann", 2))
# Note to self: This is a very good morning!

# Okay lets understand pop() method
# Removes element at a specific index.
print(new_names.pop())
print(new_names)

print(new_names.pop(4))
print(new_names)

print(new_names.pop(3))
print(new_names)


