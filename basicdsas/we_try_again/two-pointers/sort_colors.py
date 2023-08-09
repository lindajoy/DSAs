"""
Given an array, colors, which contains a combination of the following three elements:

0 (representing red)
1 (representing white)
2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, 
with the colors in the order of red, white, and blue.

The function should only return the modified colors array.

==Sample Input 1==
Example Input:
[2,2,0,1,2,2,0,2]
Example Output:
[0,0,1,2,2,2,2,2]

==Sample Input 2==
Example Input
[2,2,1,1,0]
Example Output
[0,1,1,2,2]
"""

def sortarray(colors):
    red = 0
    white = 0
    blue = len(colors) - 1

    while white < blue:
        if colors[white] == 0:
            colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1:
            if colors[blue] < colors[white]:
                colors[white], colors[blue] = colors[blue], colors[white]
            white += 1 

        else:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1

        

    return colors

a= [2,2,1,1,0]
b= [2, 1, 1, 0, 0]

print(sortarray(a))
print(sortarray(b))

