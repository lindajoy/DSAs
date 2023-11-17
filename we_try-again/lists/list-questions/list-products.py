"""
Implement a function, find_product(lst),
which modifies a list so that each index has a
product of all the numbers present in the list 
except the number stored at that index.

Input:
A list of numbers (could be floating points or integers)

Output:
A list such that each index has a product of all the numbers in the list except the number stored at that index.

Sample Input:
arr = [1,2,3,4]

Sample Output
arr= [24,12,8,6]
"""

# I was not able to come up with the solution, so I went through the suggested solutions.
# We except to recieve an input of a list consisting of floating points or integers

def find_product_1(lst):
    result = []
    left =  1 #To store product of all previous values from currentIndex

    for i in range(len(lst)):
        print(i)
        currentProduct = 1 # To store current product for index i
        # compute product of value to the right of i index of list

        for ele in lst[i + 1:]:
            print('Sliced list:', lst[i + 1:])
            currentProduct = currentProduct * ele
            print(left)
            print(currentProduct)
        result.append(currentProduct * left)

        # updating 'left'
        print('Left before update', left)
        print('Has the index been updated:', i)
        print('What is the value at that particular Index', lst[i])
        left = left * lst[i]
        print('Left after update:', left)
        
    return result


# print(find_product_1([1,2,3,4]))
print(find_product_1([2,2,3,4]))

