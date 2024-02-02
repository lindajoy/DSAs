# Sunset Views.
# First question that comes to mind; Without the direction array; say our sun is always facing west always.

def sunset_views(buildings, direction):
    # Validate your input:
    if len(buildings) == 0 or not direction:
        return "Input is invalid!"
    
    # Simplest case:
    if len(buildings) == 1:
        return [0]
    
    stack = []
    # for i, height in enumerate(buildings):
    #     while stack and height >= stack[-1][1]:
    #         stack.pop()
    #     stack.append([i, height])

    for i, height in enumerate(reversed(buildings)):
        while stack and height >= stack[-1][1]:
            stack.pop()
        stack.append([i, height])
    # print(stack)

    return [index[0] for index in stack]


# Test the function


def sunsetViews2(buildings, direction):
    result = []
    step = 1 if direction == "EAST" else -1
    start = 0 if direction == "EAST" else len(buildings) - 1
    index = start
    current_max = float('-inf')
    while index >= 0 and index < len(buildings):
        if buildings[index] > current_max:
            result.append(index)
            current_max = buildings[index]
        index += step
    return result if direction == "WEST" else result[::-1]


buildings1 = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "EAST"
print(sunsetViews2(buildings1, direction))