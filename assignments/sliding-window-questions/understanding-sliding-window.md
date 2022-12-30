# Sliding Window Technique 

Sliding window is a good technique when you need to keep track of contigous elements (elements that are next to each other).

Sliding Window Technique is a method for finding subarrays in an array that satisfy given conditions. *We do this via maintaining a subset of items as our window and resize and move that window within the larger list until we find a solution.*

Its a branch of dynamic programming is a technique that breaks a big problem into smaller subproblems, saves the result for later to avoid computing them again.

The fundamental clues  to identify problems needing this kind of technique are:
    1. Contiguous means sequential, which means the elements must be right next to each other to count as a pair. This is a **giant**  clue that a sliding window may work beautifully with this question.
    2. The problem will be based on array, list or string.
    3. It will ask to find subrange in that array or string will have to give the longest, shortest or target values.
    4. Its concept is mainly based on ideas like the longest sequence or shortest sequence of something that satisfies a given  condition perfectly.


### How does the sliding window work?
  
## Randoms From Different Questions.

#### Find-max-sliding-window.py

Deque - This is a double-ended queue where the pop and push operations work in O(1) at both ends.
It acts as our window,We will store elements in the deque in decreasing order.
The front of the deque contains the maximum value in that particular window.

### References
* [An Introduction to Sliding Window Algorithms](https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7)