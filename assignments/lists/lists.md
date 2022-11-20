# Better understanding of Lists

Lists are data structures that group different elements together. Lists can have elements of different types and you can also mix different types with the same list.

They are created by square brackets and each element is separated by (,)

Sublists are subsets of lists that can be obtained by getting a portion of the list.

A sublist can be created by writing the list name, then separating the start and end indexes with a colon.

Given a list l, to create sublist l1 and l2 write:

l= [1,2,3,4,5]

l1=l[0:3]
l2=l[3:5]

# List concatenation
print([1,2] + [3,4])

# Traversing a list
l=[1, 2, 4, 8, 10]
for val in l:
  print(val)
