"""
Write a program which takes as input two sorted arrays, 
and returns a new array containing elements that are present in both of the input arrays. 
The input arrays may have duplicate entries, but the returned array should be free of duplicates. 
For example, the input is [6,3,3,5,5,6,7,7,8,12] and [5,5,6,8 ,8,9,70,10], your output should be (5, 6, 8).
"""

print(set([2,3,3,5,5,6,7,7,8,12]))

# A good thing about this question: Is that both arrays are sorted.
# Here I am using a set

def findIntersection(arr1, arr2):
    first_ptr, sec_ptr, result = 0, 0, set()
    
    while first_ptr < len(arr1) and sec_ptr < len(arr2):
        if arr1[first_ptr] < arr2[sec_ptr]:
            first_ptr += 1
        elif arr1[first_ptr] > arr2[sec_ptr]:
            sec_ptr += 1
        elif arr1[first_ptr] == arr2[sec_ptr]:
            result.add( arr1[first_ptr])
            first_ptr += 1
            sec_ptr += 1
    return list(sorted(result))
lst1 = [2,3,3,5,5,6,7,7,8,12] 
lst2 = [5,5,6,8 ,8,9,70,10]
print(findIntersection(lst1,lst2))

# What if you were asked not to use a set?
# We will use a list instead?
def findIntersection2(arr1, arr2):
    first_ptr, sec_ptr, result = 0, 0, []
    
    while first_ptr < len(arr1) and sec_ptr < len(arr2):
        if arr1[first_ptr] < arr2[sec_ptr]:
            first_ptr += 1
        elif arr1[first_ptr] > arr2[sec_ptr]:
            sec_ptr += 1
        elif arr1[first_ptr] == arr2[sec_ptr]:
            if arr1[first_ptr] != arr1[first_ptr - 1] or arr2[sec_ptr] != arr2[sec_ptr -1]:
                result.append(arr1[first_ptr])
            # You forgot to increase the first and the second pointers.
            first_ptr += 1
            sec_ptr += 1

            
    return result
lst1 = [2,3,3,5,5,6,7,7,8,12] 
lst2 = [5,5,6,8 ,8,9,70,10]

print(findIntersection2(lst1, lst2))

