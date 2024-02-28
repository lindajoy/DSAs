"""
CONTAINER WITH MOST WATER.

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# 💡 I usually have trouble with this question.
def maxArea(heights):
    left, right = 0 , len(heights) - 1
    maxarea = 0

    while left < right:
        maxarea =  max(maxarea, min(heights[left], heights[right]) * (right - left))

        if heights[left] < heights[right]:
            left += 1
        elif heights[right] <= heights[left]:
                right -= 1
    return maxarea
    
print(maxArea([1,8,6,2,5,4,8,3,7]))