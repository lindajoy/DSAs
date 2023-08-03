"""
Given a string add(3,4) return 7
Assume that it will always be addition

Assumptions: The input will always be add(10,4)
             Strongly testing String Manipulation
PSEUDOCODE:
  1. We slice the string from index 4 since we know from that index, the numbers will always follow.
  2. Replace the ")" with " "
  3. When we use split we create a list of those elements
  4. Convert them into integers 
  5. Return the sum.
"""

"""
💡 INPUT: String (add(3,4))
💡 OUTPUT: 7
"""
a = "add(10,4)"
b = "add(3,5)"
c = "add(15,13)"
def addTwoNumbers(string):
    # First thinking is we can slice the string...add(10,4)
    a = string[4:] # This will give 10,4
    # Next step would be to remove the , from 3,4 
    a = a.replace(')', '')
    number_as_strings = a.split(",")
    numbers = [int(num) for num in number_as_strings]
    return sum(numbers)

print(addTwoNumbers(b))
print(addTwoNumbers(a))  
print(addTwoNumbers(c))        

