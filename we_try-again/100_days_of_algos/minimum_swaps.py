'''
MINIMUM NUMBER OF SWAPS.

You are given a 0-indexed string s of even length n. 
The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.
    You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

'''

# Did not try as much in this question as i hoped to

# Whats the input? The input is a string.
# Whats the output? Minimum number of swaps

import math

def minimumNumberOfSwaps(s):
    count = 0
    stack = []
    
    for ch in s:
        if ch == '[':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                count += 1
    return math.ceil(count / 2)

print('Example One: ',minimumNumberOfSwaps('][]['))
print('Example Two: ', minimumNumberOfSwaps(']]][[['))

    