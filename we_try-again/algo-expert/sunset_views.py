"""
SUNSET VIEWS

Given an array of buildings and a direction that all of the buildings face, return an array of the indices of the buildings that can see the sunset.
A building can see the sunset if it's strictly taller than all of the buildings that come after it in the direction that it faces.

The input array named buildings contains positive, non-zero integers representing the heights of the buildings. 
A building at index i thus has a height denoted by buildings[i].
All of the buildings face the same direction, and this direction is either east or west, denoted by the input string named direction, 
which will always be equal to either "EAST" or "WEST". 
In relation to the input array, you can interpret these directions as right for east and left for west.

Important note: the indices in the ouput array should be sorted in ascending order.

"""
# Whats the input? An array of buildings and the direction that all of the buildings face.
# Output? An array of indices of the buildings that can see the sunset.
# 💡 A building can see the sunset if its strictly taller than all of the buildings that come after it in the direction it faces.

# INPUT: An array of builds containing positive, non-zero integers.
def sunset_buildings(buildings, direction):
    n = len(buildings)
    visible_indices = []

    if direction == "EAST":
        # Iterate from the end towards the beginning
        for i in range(n - 1, -1, -1):
            visible = True
            for j in range(i + 1, n):
                print(buildings[i])
                print(buildings[j])

                if buildings[i] <= buildings[j]:
                    visible = False
                    break
            if visible:
                visible_indices.append(i)
    elif direction == "WEST":
        # Iterate from the beginning towards the end
        for i in range(n):
            visible = True
            for j in range(i):
                if buildings[i] <= buildings[j]:
                    visible = False
                    break
            if visible:
                visible_indices.append(i)

    return sorted(visible_indices)

# Example usage:
buildings = [3, 7, 8, 3, 6, 1]
direction = "WEST"
buildings2 = [3, 5, 4, 4, 3, 1, 3, 2]
direction2 = "EAST"
# print(sunset_buildings(buildings2, direction2))  # Output: [1, 2, 4, 5]

# SUNSET VIEWS

# O(N) time and space
def sunsetViews3(buildings, direction):
    result = []
    
    step = 1 if direction == "EAST" else -1
    start = 0 if direction == "EAST" else len(buildings) - 1
    
    index = start
    print("Starting Index", index)
    while index >= 0 and index < len(buildings):
        print(index)
        height = buildings[index]


        while len(result) > 0 and buildings[result[-1]] <= height:
            print('buildings index:', buildings[result[-1]])

            result.pop()
            
        result.append(index)
        index += step
        
    return result if direction == "EAST" else result[::-1]
buildings2 = [3, 5, 4, 4, 3, 1, 3, 2]
direction2 = "EAST"
print(sunsetViews3(buildings2, direction2))


# O(N) time and space
def sunsetViews(buildings, direction):
    result = []
    
    step = 1 if direction == "WEST" else -1
    start = 0 if direction == "WEST" else len(buildings) - 1
    
    index = start
    currentMax = float('-inf')
    while index >= 0 and index < len(buildings):
        if buildings[index] > currentMax:
            result.append(index)
            currentMax = buildings[index]
            
        index += step
        
    return result if direction == "WEST" else result[::-1]