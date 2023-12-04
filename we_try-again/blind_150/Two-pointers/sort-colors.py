"""
Given an array, colors, which contains a combination of the following three elements:
0 (representing red)
1 (representing white)
2 (representing blue)
Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red, white, and blue.
"""

"""
😢 Pretty much struggled through this one....

# First iteration does not work 💔
"""
# def sort_colors(colors):
    # red = 0
    # white = 0
    # blue = len(colors) - 1

    # # Sort the edge cases first
    # if len(colors) == 1:
    #     return colors
    
    # # sort if len colors == 2
    # if len(colors) == 2:
    #     if colors[1] < colors[0]:
    #         colors[0], colors[1] =colors[1], colors[0]
    #     elif colors[1] == colors[0]:
    #         return colors

    # while white < blue:
    #     if colors[white] == 0:
    #         colors[red], colors[white] = colors[white], colors[red]
    #         red += 1
    #         white += 1
    #     elif colors[white] == 1 and colors[white] > colors[blue]:
    #         colors[white], colors[blue] = colors[blue], colors[white]
    #         white += 1
    #     elif colors[white] == 1 and colors[white] < colors[red]:
    #         colors[white], colors[red] = colors[red], colors[white]
    #         white += 1
    #     elif colors[white] == 2:
    #         colors[blue], colors[white] = colors[white], colors[blue]
    #         blue -= 1

    # return colors


# Second Solution: This is much better; Works better

def sort_colors_2(colors):
    red, blue = 0, len(colors) - 1
    i = 0

    while i <= blue:
        if colors[i] == 0:  # If the current element is red
            colors[i], colors[red] = colors[red], colors[i]
            red += 1
            i += 1
        elif colors[i] == 2:  # If the current element is blue
            colors[i], colors[blue] = colors[blue], colors[i]
            blue -= 1
        else:  # If the current element is white (1), move to the next element
            i += 1
    return colors
    


print(sort_colors_2([0, 1, 0]))
print(sort_colors_2([1, 1, 0, 2]))
print(sort_colors_2([2, 2]))

# QuickSort Algorithm: Quite interesting 🤔
# This is a divide and conquer algorithm.
# How quick sort works:
# 1. Choose an element or the pivot index, It can be anything
# 2. Elements that are less than the pivot index go to the left of the pivot index, greater than the element go to the right of the index.
# 3. Passing the smaller lists as an array.
# 4. Join the sorted arrays that are returned from the recursive call and the pivot

RED, WHITE, BLUE = range(3)

def dutch_flag_sort(colors):
    pivot_index = len(colors) // 2
    pivot = colors[pivot_index]

    smaller = 0
    # First pass: Group elements smaller than pivot
    for i in range(len(colors)):
        # look for a smaller element.
        if colors[i] < pivot:
            colors[i], colors[smaller] = colors[smaller],colors[i]
            smaller += 1
    
    larger = len(colors) - 1
    for i in reversed(range(len(colors))):
        if colors[i] < pivot:
            break
        elif colors[i] > pivot:
           colors[i], colors[larger] = colors[larger],colors[i]
           larger -= 1
    return colors

print(dutch_flag_sort([1, 1, 0, 2]))
print(dutch_flag_sort([1, 1, 0, 2]))
print(dutch_flag_sort([2, 1, 1, 0, 0]))





