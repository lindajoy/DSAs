"""

Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is 
the smallest in lexicographical order
among all possible results.

Example : 
Input: s = "bcabc"
Output: "abc"

Input: s = "cbacdcbc"
Output: "acdb"
"""


def remove_duplicates(str):
    stringSet = set()

    for i in str:
        stringSet.add(i)

    s = sorted(stringSet)

    return ''.join(s)


print(remove_duplicates('bcabc'))


"""
Print out repetitive letters

codility
"""

def printRepetitive(s):
    stringSt = []
    cache = []

    for i in s:
        if(i) in stringSt:
            cache.append(i)
        else:
            stringSt.append(i)

    return ''.join(cache)

print(printRepetitive('codility'))