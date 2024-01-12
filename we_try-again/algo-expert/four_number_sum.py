"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order.
If no four numbers sum up to the target sum, the function should return an empty array.
"""
# 💡 Whats the input? An array of numbers and a target sum.
# 💡 All the possible quadraplets that sum up to the target sum.

def fourNumberSum(numbers, target):
    quadruplets = []
    hashTable = {}

    for i in range(1, len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            currentSum = numbers[i] + numbers[j]
            difference = target - currentSum

            if difference in hashTable:
                for pair in hashTable[difference]:
                    quadruplets.append(pair + [numbers[i], numbers[j]])

        for k in range(0, i):
            print("My second i", i)
            print('My K', k)
            currentSum = numbers[k] + numbers[i]

            if currentSum not in hashTable:
                hashTable[currentSum] = [[numbers[k], numbers[i]]]
            else:
                hashTable[currentSum].append([numbers[k], numbers[i]])

    return quadruplets

print(fourNumberSum([7, 6, 4, -1, 1, 2], 16))