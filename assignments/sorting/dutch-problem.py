RED,  WHITE, BLUE = range(3)
print('🟥',RED)
print('⬜️',WHITE)
print('🟦',BLUE)


def dutch_flag_sort(arry):
    low = 0
    mid = 0
    high = len(arry) - 1

    while mid <= high:
        if arry[mid] == 0:
            arry[low], arry[mid] = arry[mid], arry[low]
            low += 1
            mid += 1

        elif arry[mid] == 1:
            mid += 1

        else:
            arry[high], arry[mid] = arry[mid], arry[high]
            high -= 1

    return arry
