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
