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

