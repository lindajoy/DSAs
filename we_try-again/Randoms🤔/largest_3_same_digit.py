"""
You are given a string num representing a large integer.
An integer is good if it meets the following conditions:
    It is a substring of num with length 3.
    It consists of only one unique digit.

Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

"""
Input: A string input
Output: A string output with 3 digits
"""

# This solution works for other inputs but when it comes to this one "2300019"
# It ouputs a "0"  instead of "000"
def largestGoodInteger(num:str) -> str:
    left = 0
    right = left + 3
    res = ""
    while right < len(num):
        sample_str = num[left: right]
        sample_set = set(sample_str)
        if len(sample_set) == 1:
            res = max(res, sample_str)
        left += 1
        right = left+3
    return res
print(largestGoodInteger("2300019"))

def largestGoodInteger2(num: str) -> str:
    res = ""
    for i in range(len(num) - 2):
        sample_str = num[i:i + 3]
        sample_set = set(sample_str)
        if len(sample_set) == 1:
            res = max(res, sample_str)
        return res


res = ''
s= "222"

k = max(res, s)
print(k)


        



