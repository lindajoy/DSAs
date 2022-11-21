'''
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.

Name it merge_lists(lst1, lst2).

list1 = [1,3,4,5]  
list2 = [2,6,7,8]

sample_output: arr = [1,2,3,4,5,6,7,8]

Inputs: Two lists
Otput: One sorted list

'''

'''
💡 Naive Approach
'''
def merge_two_lists(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3


print(merge_two_lists([1,3,4,5],[2,6,7,8]))

'''
💡 Data Struture Approach (as if there's a big difference 😁)
'''
def merge_lists(list1, list2):
    # Assigning ptr1 and ptr2 to value 0
    ptr1 = ptr2 = 0

    # Do a check if the index is always less than the length of the list
    while (ptr1 < len(list1) and ptr2 < len(list2)):
        # If the value at that specific index in list1 is greater than the value in the value at the same level in list1
        # Insert the number at the index => Insert(index, specific element)
        # Increase the index value on both ptr and ptr2
        if list1[ptr1] > list2[ptr2]:
            list1.insert(ptr1, list2[ptr2])
            ptr1 += 1
            ptr2 += 1
        else:
            ptr1 += 1

    # Why did you do this?
    if ptr2 < len(list2):
        list1 += list2[ptr2:]    
    return list1
    

print(merge_lists([1,3,4,5],[2,6,7,8]))