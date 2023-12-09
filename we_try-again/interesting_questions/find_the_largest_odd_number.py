"""
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num,
or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

Input = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.

Something you need to remember is that strings in Python are iterables!!
"""

# First solution is the brute force algorithm that has two loops:
# The first loop; we are looping through the first loop
# The second loop: we are looping from the second index within the length of the string
# First solution is quite unhealthy: The time complexity of this solution is O(n)2 equating to a quadratic solution.
def find_largest_odd_number(string):
    res = 0

    def is_odd(num):
        return int(num) % 2 != 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            integer = string[i:j]
            if is_odd(integer):
                if int(res) < int(integer):
                    res = integer

    return res if res != 0 else ''

## Hehe, Did you know when you slice a string and the last index might be out of bound; 
# It will still slice the string well
# Example 1

# This string indexes from 0 to 6
random_string2 = "annrita"

# Lets slice the string
print('Hello! Random Sliced String:', random_string2[4: 10])


# print(find_largest_odd_number("4206"))
# print(find_largest_odd_number("35427"))


# def find_largest_odd_number2(string):
#     res = 0

#     for i in range(len(string)):
#         for j in range(i+1, len(string) + 1):
#             print('here is the value of J', j)
#             print('here is the value of I', i)

# print(find_largest_odd_number2("35427"))


# 💡 Second Solution

def largestOddNumber(num):
    for i in range(len(num) -1, -1, -1):
        print(num[i])
        if i%2 == 0:
            print(i)
            return num[:i+ 1]
    return ""

print(largestOddNumber("123456"))
print(largestOddNumber("35427"))
print(largestOddNumber("52"))

# Lets try to understand something...

random_string_3 = "WawiraJoy"

for i in range(len(random_string_3)- 1, -1, -1):
    # When looping through an array it will always start from the end index.
    # So here the end index is 8
    # it will start from 8 going towards the start
    # the end value is 0;

    print('Random character in my string: ',random_string_3[i])
  
   
random_int = 123

print(random_int[0])
