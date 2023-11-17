"""
Implement a function, find_first_unique(lst) that returns the first unique integer in the list.

Input: A list of integers

Output: The first unique element in the list
"""
# 💡 FIRST IMPLEMENTATION

# This would work for this case, However, we have to also consider cases where the first unique element
# Might not be at index 0; Eg consider input [4,5,1,2,0,4]

lst = [9,2,3,2,6,6]
print(set(lst))

# 💡 SECOND IMPLEMENTATION (Using Count)
def findFirstUnique(lst):
    for x in lst:
        if list.count(x) == 1:
            return x
    return None

# 💡 Third implementation. (Enumerate)

def findFirstUnique2(lst):
    for i, x in enumerate(lst):
        if x not in lst[:i] + lst[i+1:]:
            return x
        
print(findFirstUnique2([4, 5, 1, 2, 0, 4]))

# 💡 Fourth Implementation. (Dictionary!) 😁 Why did I not think about this before?
def findFirstUnique3(lst):
    # Initialize a dictionary
    counts = {}

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    for item in lst:
        if counts[item] == 1:
            return item
    return -1

print(findFirstUnique3([4, 5, 1, 2, 0, 4]))
