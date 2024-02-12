"""
Reverse A Single Sublist

Write a program which takes a singly linked list L and two integers s and / as arguments, and reverses the order of the nodes from the sth node to /th node, inclusive. 
The numbering begins at 1., i.e., the head node is the first node. Do not allocate additional nodes.

"""

# 💡 I found this question interesting: Following up on reversing a linked list entirely

# Whats the input? Linked list, starting, finish point
# Whats the output? Linked list; with the modified reversal.

# Hmm the problem is I am not sure I understand..

# Class initializes the components of a linked list.
class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def reverse_sublist(L, start, finish):
    # Initialize variables that will be used 
    dummy_head = sublist_head = ListNode(0,L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next , sublist_head.next = (temp.next, sublist_head.next, temp)

    return dummy_head.next


# Lets go back and assume that it was a list?
# You are given a list, and a starting and ending point of the slice that should be reversed.
# Example: [1,2,3,4], starting = 2, ending = 3
# Output: should be: [1,2,4,3]
# 💡 Another example would be:
# [4,5,5,7,8], starting = 2, ending 2
# Remains the same.

def reversing_a_list_portion(l, startingPoint, endingPoint):
    if startingPoint == endingPoint:
        return l
    
    # Before does not include that specific index.
    first_slice = l[:startingPoint]
    # After includes that index
    second_slice = l[startingPoint:]

    left = 0
    right = len(second_slice) - 1

    while left < right:
        second_slice[left], second_slice[right] = second_slice[right], second_slice[left]
        left += 1
        right -= 1

    # This commented line would not work hehe; Isn't that intersting?🤔
    # return first_slice.extend(second_slice)
    first_slice.extend(second_slice)

    return first_slice
    
print(reversing_a_list_portion([1,2,3,4], 2, 3))
print(4%1)