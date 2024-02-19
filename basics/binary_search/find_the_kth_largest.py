"""
💡 FIND THE KTH LARGEST ELEMENT

Given an input array A = [3,2,1,5,4] Return the  3rd largest element
This is 3.
"""

# 💡 Brute Force Solution

# We can easily sort the array in descending order: So that we have something like this:
# [5, 4, 3, 2, 1]

# The time complexity of this would be O(n log n)
# N is the length of the array/ list 😄
# Best case: O(N)

def find_k_largest_element(A, k):
    sorted_array = sorted(A, reverse= True)
    return sorted_array[k - 1]

print(find_k_largest_element([3,2,1,5,4], 3))


# 💡 Using a heap
# Hmm this is an interesting way of solving it. 🤔

# Pseudocode:
#
#   i) Initialize a heap
#   ii) We push every number into our heap
#   iii) We remove values (This are the smallest elements) from our heap while the length of the heap is greater than k
#   iv) After that is done we return the smallest element which equates to our result.

import heapq

def find_k_largest_element_heap(A, k):
    heap = []
    
    for num in A:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)

# What if i was sort the elements in place without completely sorting the array.

# Introducing our subroutine:

# A subroutine is a set of programs that are repeatedly used within a program
# It allows a programmer to reuse a set of instructions in multiple parts of the program.

# Is O(log n) always faster than O(n)? 🤔

# Coding solution: This is about to get a little heavy!

def find_kth_largest_optimal(nums, k):
   # Our helper function => Quicksort Algorithm
   def partition(nums, left, right):
       pivot, fill = nums[right], left

       for i in range(left, right):
           if nums[i] <= pivot:
               nums[fill], nums[i] = nums[i], nums[fill]
               fill += 1
       nums[fill], nums[right] = nums[right], nums[fill]

       return fill
   
   k = len(nums) - k
   left, right = 0, len(nums) - k

   while left < right:
       pivot = partition(nums, left, right)

       if pivot < k:
           left = pivot + 1
       elif pivot > k:
           right = pivot - 1
       else:
           break
   return nums[k]

# There is something intersting, I saw in the EOP solution though it was hard to follow.
import random
left , right = 0, 10
# This can help in selecting the pivot element if ever given the choice to do it.
print(random.randint(left,right))

# The third solution: Comes with a long concept I have never checked out in a while: 🤹🏾‍♀️ QUICKSORT ALGORITHM.

"""
QUICKSORT ALGORITHM: This is a divide and conquer algorithm 🤔

Quicksort is a sorting algorithm based on the divide and conquer approach where:

    1. An array is divided into subarrays by selecting a pivot element(element selected element)
       Elements less than the pivot should be positioned in such a way elements are kept on the left side
       and elements greater are on the right side of the pivot
    
    2. The left and right subarrays are also divided using the same approach. The process continues untill each subarray
        cointains a single element

    3. At this point, elements are already sorted. Finally elements are combined to form a sorted array.
"""
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array:", data)
size = len(data)
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending Order:", data)