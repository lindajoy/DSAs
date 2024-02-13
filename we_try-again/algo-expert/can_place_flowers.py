"""
💡 CAN PLACE FLOWERS

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

# Hehe this is an easy question.

# A little bit difficult than it looks..🤔
# My First solution fails on the third example.

# Whats is the input? An array flowerbed, and number of flowers
# What is the output? Boolean.

# Something I am thinking about is we can do is initialize a left and right pointer
# Loop through the entire array by always checking its neighbors.

# Since we are looping through each member in an array: The time complexity would be O(N)

def canPlaceFlowers(flowerbed, number_of_flowers):
    # Validate the inputs
    if not flowerbed:
        return  False
    if number_of_flowers > len(flowerbed):
        return False
    
    # 💡 We add this line since this is not a cyclic flowerbed; The flowers are arranged in a straight line.
    flowerbed = [0] + flowerbed + [0]

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] != 1 and flowerbed[i + 1] != 1 and flowerbed[i - 1] != 1:
            number_of_flowers -= 1
            flowerbed[i] = 1

    print(flowerbed)
    print(number_of_flowers)

    return number_of_flowers <= 0

print(canPlaceFlowers([0,0,1,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,0,1], 2))





