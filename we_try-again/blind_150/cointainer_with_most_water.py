"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container
"""
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# 💡 This solution uses the two pointers pattern

def max_Area(heights):
    max_area = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        area = (right - left) * min(heights[right], heights[left])
        max_area = max(area, max_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

# print(max_Area([1,8,6,2,5,4,8,3,7]))
# print(max_Area([1,2,1]))
print(max_Area([4,3,2,1,4]))