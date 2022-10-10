

def quickSort(array):
    quick_sort_helper(array, 0 , len(array)-1)
    return array

def quick_sort_helper(array, start ,end):
    if start >= end:
       return

    pivot = start
    # position every number in the array in the sorted order with respect to the array[pivot]
    # left and right to stop at a place where: left <= pivot and right >= pivot

    left = start + 1
    right = end

    while left <= right:
        # check if can swap
        if array[left] > array[pivot] and array[right] < array[pivot]:
            array[left] , array[right] = array[right], array[left]

        # cannot swap
        elif array[left] <= array[pivot]: #no need to be swaped
            left += 1
        else:
            right -= 1

        # place pivot at the correct position(right)
        # we know that once the sorting is done, the numbers at left will be <= pivot and right >= pivot
        # smaller values go to the left of the array[pivot]
        array[pivot], array[right] = array[right] , array[pivot]

        # sort to the left and right of array[pivot]
        if(right - 1, start) < (end -right-1):
            quick_sort_helper(array, start, right - 1)
            quick_sort_helper(array, right + 1, end)
        else:
            quick_sort_helper(array, right + 1, end)
            quick_sort_helper(array, start, right - 1)

sorted_array = [1,6,7,3,4]
result2 = quickSort(sorted_array)
print(result2)


        