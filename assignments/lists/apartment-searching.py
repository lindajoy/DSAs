"""
You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.

You also have a list of requirements: a list of buildings that are important to you. 
For instance, you might value having a school and a gym near your apartment. 
The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. 
For instance, for every block, you might know whether a school, a pool, an office, and a gym are present.

In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and 
a list of your required buildings and that returns the location (the index) of the block that's most optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.


"""
import math
blocks = [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]

reqs = ["gym", "school", "store"]

def find_optimal_apartment(blocks, required_buildings):
    num_blocks = len(blocks)
    max_distances = [0] * num_blocks

    # Loop through Blocks
    for i in range(num_blocks):
        # Looping through the required buildings
        for building in required_buildings: 
            # check if the certain bulding you are looking for is on the block
            if blocks[i][building] == False or building not in blocks[i]: 
                # Initialize the nearest block tto float(inf)
                nearest_block = float("inf")
                # Loop throug the num_blocks again
                for j in range(num_blocks):
                    if blocks[j][building] == True or building not in blocks[j]:
                        # Get the nearest block by getting the minimum value
                        nearest_block = min(nearest_block, abs(j-i))
                # Return the maximum distance
                max_distances[i] = max(max_distances[i], nearest_block)

    # Find the block with the maximum minimum distance
    min_distances = min(max_distances)
    print(min_distances)
    for i in enumerate(max_distances):
        print(i)
    
    # Find the optimal block
    optimal_blocks = [i for i , distance in enumerate(max_distances) if distance == min_distances]
    print(optimal_blocks)
    return optimal_blocks[0]

print(find_optimal_apartment(blocks, reqs))