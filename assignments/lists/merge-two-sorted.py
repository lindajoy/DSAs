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
    # Assigning ptr1 and ptr2 to value 0 (To read from index 0)
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
        list1 += list2[ptr2:]  # Append whatever is left of list2 to list1
    return list1
    

print(merge_lists([1,3,4,5],[2,6,7,8]))

'''
Solution Analysis

The solution merges two lists in place, no new list is created.

We set the index to start reading from index 0 -> Then compare the elements of both.

If the current element in the first list is greater than the element in the second list.

insert the current element of the second list in place of 
the current element of the first list and increment both index variables by 1.

Note that the insert operation is done using the built-in insert function.

However, if the current element of the first list is smaller than the current element of the second list,
then only increment the index variable of the first list by 1. 

After that, if the index of the second list is smaller than the length of the list,
extend the first list by the second one from that index until the end.
'''


# Time Complexity

'''
Since both lists are traversed in this solution as well, the time complexity is O(m(n+m)) 
where n and m are the lengths of the lists. Both lists are not traversed separately
so we cannot say that complexity is (m+n). The shorter of the two lengths is traversed in the while loop. 
Also, the insert function gets called when the if-condition is true. 
In the worst-case, the second list has all the elements that are smaller than the elements of the first list. In this case, the complexity will be O(mn)

'''