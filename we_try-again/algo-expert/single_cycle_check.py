"""
You're given an array of integers where each integer represents a jump of its value in the array. 
For instance, the integer 2 represents a jump of two indices forward in the array; 
the integer -3 represents a jump of three indices backward in the array.

If a jump spills past the array's bounds, 
it wraps over to the other side. 
For instance, a jump of -1 at index 0 brings us to the last index in the array. 
Similarly, a jump of 1 at the last index in the array brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle. 
A single cycle occurs if, starting at any index in the array and following the jumps, 
every element in the array is visited exactly once before landing back on the starting index.

array = [2, 3, 1, -4, -4, 2]
Output = Should be true.
"""
# Challenge when solving this question was:
#   1. I did not understand what the question was asking at first

# PROBLEM BREAKDOWN 💪🏻
"""
Given the input: [2, 3, 1, -4, -4, 2], If we start at index 0:
    i) We will land at 1
    ii) After landing at  1, we will go to the first (-4)
    iii) Then we will land at the last element 2
    iv) Then we will land at index 1 (Which is 3)
    v) Then we will land again at the last(-4)
    v) -4 will take us back to index 2
"""

# Questions for the interviewer
# 1. Just to clarify, when we start at any particular index, we expect to return to that index after visiting each Element in the array?

# Considering this there are three conditions we need to track.
#   1. We need to visit n number of elements where n = array.length
#   2. If, after we have visited every element, we are not back at the starting point, we have a problem
#   3. If we have visited more than one element, and not yet visited every other element (1<n<array.length), and we find ourselves back at the starting point, we have a problem

# Time Complexity: Is likely to be O(n),n being the length of the array.
# Space complexity: Will be O(1) because we are not creating any additional arrays or structures that are dependent on the input size.

# Whats the input? An Array
# Whats the output? A boolean 


def hasSingleCycle(array):
    # We keep track of the visited elements
    numVisited = 0
    # We begin our journey at the end of the list; We can start the current Index at any point.
    # You can Opt to start at the beginning, middle or end 🙃
    currentIndex = len(array) - 1

    def findNextIndex(current, array):
        leap = array[current]
        # 💡 Interesting way of looking for our next index. This is one trick you should have for similar problems.
        nextIndex  = (current + leap) % len(array)
        if (nextIndex >= 0):
            return nextIndex
        else:
            return nextIndex + len(array)
        
    # We create a loop such that it continues to loop 
    # if the number of visited is less than the length of the array
    while (numVisited < len(array)):
        # If the number of visited is greater than 0 and we are already back to our currentIndex:
        # Meaning that we have not visited every element in the array.
        if (numVisited > 0 and currentIndex == len(array) - 1):
            return False
        numVisited += 1
        currentIndex = findNextIndex(currentIndex, array)
    return currentIndex == len(array) - 1

print(hasSingleCycle([2, 3, 1, -4, -4, 2]))

