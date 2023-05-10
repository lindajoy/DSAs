# Start with the middle element:
# If the target value is equal to the middle element of the array, then return the index of the middle element.
# If not, then compare the middle element with the target value,
# If the target value is greater than the number in the middle index, then pick the elements to the right of the middle index, and start with Step 1.
# If the target value is less than the number in the middle index, then pick the elements to the left of the middle index, and start with Step 1.
# When a match is found, return the index of the element matched.
# If no match is found, then return -1

list = [1,2,3,4,5,6]

size = len(list)
print(size)
print('Hello World')

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high // 2 
        guess = list[mid]
        print('Here is the mid-value:', guess)

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        
        else:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9]
print (binary_search(my_list, 3))

