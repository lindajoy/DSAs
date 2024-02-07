"""
Monotonic Array

Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing.

Non-increasing elements aren't necessarily exclusively decreasing; t
hey simply don't increase. Similarly, non-decreasing elements aren't necessarily exclusively increasing; they simply don't decrease.

Note that empty arrays and arrays of one element are monotonic.

# Example one
Input:[1, 2, 3, 4, 5]
Output: True

# Example Two
Input: [5, 4, 3, 2, 1]
Output: True

Example 3
Input: [1, 3, 2, 5, 4]
Output: False

Example 4 

Input: [2,2,3,4,5]
Ouput: True

"""
# What is the input? An array
# What is the output? Boolean

# Time complexity is O(n); n being the length of the numbers
# Space complexity is O(1) 

def isMonotonicArray(nums):
    isDecreasing, IsIncreasing = False, False
    left, right = range(2)

    while right < len(nums) - 1:
        if nums[left] < nums[right]:
            IsIncreasing = True
        elif nums[left] > nums[right]:
            isDecreasing = True
        left += 1
        right += 1

 
    if isDecreasing and nums[right] > nums[left]:
        return False
    elif IsIncreasing and nums[right] < nums[left]:
        return False
        
    return True

    
print(isMonotonicArray([1, 3, 2, 5, 4]))
print(isMonotonicArray([1, 1, 1, 1, 1]))
print('Should return False:',isMonotonicArray([1, 1, 4, 5, 3]))
print(isMonotonicArray([5, 4, 3, 3, 2, 2, 1]))
print(isMonotonicArray([5, 3, 2, 4, 1]))
print(isMonotonicArray([[-1, -5, -10, -1100, -1100, -1101, -1102, -9001]]))

# I have been struggling with the concept of break and continue in the if statements.
for i in range(5):
    if i == 2:
        print(i)
        continue

# Initialize count to 0, while 
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
    print(count)

# This does not print out "i"; This skips (i).
# The continue statement can be used if you need to skip the current iteration of a for or while loop and move to the next iteration.
for letter in "Jessica":
    if letter == "i":
        continue
    print(letter) # This prints out: 'J', 'e', 's', 's', 'c', 'a'


num = 5
# This code breaks when the value 9 is reached: 
# So it will print out the following: 5,6,7,8
while num < 20:
    print('Current Number:', num)
    num = num + 1
    if num == 9:
        break

# Break statement if you need to break out of a for loop and move onto the next section of code.
for letter in "freeCodeCamp":
    print('letter:', letter)

# Loops through the string: freeCodeCamp
# If the value is eqal to o then we break out of the loop
# So this prints something like this: "f", "r", "e", "e", "C"
for letter in "freeCodeCamp":
    if letter == "o":
        break
    print('letter:', letter)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, '*', n // x)
            break
        else:
            print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print('Found an even number')
        continue

# Another thing I learnt today, is about sorting
# Say you have an array that looks like this
    
array_input1 = [['bianca', 40] , ['Leon', 41] , ['Mel', 54], ['Frodo', 100], ['Gandalf', 300 ]]
sorted_array = sorted(array_input1, key=lambda x: x[1])
print("Sorted Array:", sorted_array)
sorted_reverse = sorted(array_input1, key=lambda x: x[1], reverse=True)
print("Sorted in reverse:", sorted_reverse)
