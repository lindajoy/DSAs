"""
Implement a function that merges two sorted lists of m and n elements respectively, 
into another sorted list. Name it merge_lists(lst1, lst2).

Input
Two sorted lists.

Output
A merged and sorted list consisting of all elements of both input lists.

Sample Input
list1 = [1,3,4,5]  
list2 = [2,6,7,8]

Output
arr = [1,2,3,4,5,6,7,8]


"""
# FIRST ITERATION
# 🐛 There's a bug in the code since we are not accomodating, two arrays with different lengths.

def merge_lists(list1, list2):
    p1, p2 = 0, 0
    merged_list = []

    # Check if one of the lists may be empty
    if len(list2) == 0:
        return list1
    
    if len(list1) == 0:
        return list2

    while p1 < len(list1) and p2 < len(list2):
        print('P1:', p1, 'P2:', p2)
        if list1[p1] < list2[p2]:
            merged_list.append(list1[p1])
            merged_list.append(list2[p2])
        else:
            merged_list.append(list2[p2])
            merged_list.append(list1[p1])

        p1 += 1
        p2 += 1
    return merged_list

print(merge_lists([-133, -100, 0, 4],[-2000, 2000]))

# SECOND ITERATION: Fixing bugs on the first code snippet above

def merge_lists_two(lst1, lst2):
    # Initialize the first pointers, both starting at index 0
    P1, P2 = 0, 0
    merged = []

    while P1 < len(lst1) and P2 < len(lst2):
        if lst1[P1] < lst2[P2]:
            merged.append(lst1[P1])
            P1 += 2
        elif lst1[P1]  > lst2[P1]:
            merged.append(lst1[P2])
            P2 += 2
        else: 
            merged.append(lst1[P1])
            merged.append(lst2[P2])
            P1 += 1
            P2 += 2

        # Check if one of the lists may be empty
        if len(lst2) == 0:
            return lst1
        
        if len(lst1) == 0:
            return lst2

        if P1 > P2:
            return merged + lst2[P2:]
        else:
            return merged + lst1[P1:]


   