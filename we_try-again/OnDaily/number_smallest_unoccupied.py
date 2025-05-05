""" 
The Number of the Smallest Unoccupied Chair

Leetcode link: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

There is a party where n friends numbered from 0 to n - 1 are attending. 

There is an infinite number of chairs in this party that are numbered from 0 to infinity.
When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. 
If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], 
indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. 
All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.
"""
# A few things to note here:
#       1. Arrival time will always be distinct.

# 💡 Example 1:
# Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
# Output: 1

# 💡 Example 2:
# Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
# Output: 1

# What is the input? An array indicating arrival time and leaving time

# This is a heap problem apparently..🤔

""" 
The heap is used when you want to remove the highest or lowest order priority elements.
The heap allows quick access to these elements in O(1) time. However, the leap only provides quick access to the lowest or greatest elements;
finding other elements takes O(n) time since the heap is not ordered(we must iterate through the nodes).
"""

# Creating a heap
import heapq

arr = [9,7,2,8,6]

# Use heapify to convert arr into a heap
heapq.heapify(arr)

# Returns = [2, 6, 9, 8, 7]
print('Here is my heap:', arr)
# Returns = [2]
print('Here is my heap:', arr[0])

# Inserting into heap
print('I am inserting to my heap:')
arr.append(3)
print('Here is my heap after appending 3:', arr)

# Returns = [2, 6, 9, 8, 7, 3]

# Convinced to think that heaps and lists have the same methods? 🤔
# Heapify the array agin
heapq.heapify(arr)
print('Heapifying sort of like sorts the array',arr)

# Push elements into the heap
heapq.heappush(arr, 11)
print('Inserted 11',arr)

# Popping elements.
poppedElement = heapq.heappop(arr)
print('My popped element', poppedElement)
print("After removing my element", arr)


