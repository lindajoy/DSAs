"""
Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
Name it merge_lists(lst1, lst2).

Input 
Two sorted lists.

Output 
A merged and sorted list consisting of all elements of both input lists.

Sample Input 
list1 = [1,3,4,5]  
list2 = [2,6,7,8]

Sample Output
arr = [1,2,3,4,5,6,7,8]
"""
list1 = [1,3,4,5]  
list2 = [2,6,7,8]

arr = [1,2,3,4,5,6,7,8]

def merge_two_lists(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return list2
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    
    # Initialize pointers
    list1Pointer, list2Pointer = 0, 0
    merged_list = []

    while list1Pointer < len(list1) and list2Pointer < len(list2):
        if list1[list1Pointer] < list2[list2Pointer]:
            merged_list.append(list1[list1Pointer])
            list1Pointer += 1
        elif list2[list2Pointer] < list1[list1Pointer]:
            merged_list.append(list2[list2Pointer])
            list2Pointer += 1
        elif list2[list2Pointer] == list1[list1Pointer]:
            merged_list.append(list2[list2Pointer])
            merged_list.append(list1[list1Pointer])
            list1Pointer += 1
            list2Pointer += 1


    if list2Pointer < len(list2):
        sliced_l2 = list2[list2Pointer:]
        merged_list.extend(sliced_l2)

    if list1Pointer < len(list1):
        sliced_l1 = list1[list2Pointer:]
        merged_list.extend(sliced_l1)

    return merged_list


print(merge_two_lists(list1, list2))
print(merge_two_lists([-133, -100, 0, 4],[-2000, 2000]))
print(merge_two_lists([4, 4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4, 4]))
print(merge_two_lists([],[1, 2, 3, 4, 5]))
print(merge_two_lists([1, 4, 45, 63],[]))
print(merge_two_lists([],[]))



        


