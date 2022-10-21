"""
The Question is:

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1: Input: haystack = "sadbutsad", needle = "sad"
           Output: 0


Example 2:  haystack = "leetcode", needle = "leeto"
           Output : -1
"""

"""
💡 Substring Operations In Python
"""
some_string = 'leetcode'
print('leeto' in some_string)
if('leeto' not in some_string):
    print(-1)
else:
    print(1)


def needleHayStack(haystack, needle):
    start, end = 0, len(haystack) -1
    count = 0
   
    if (needle not in haystack):
        return -1
        

    while (start < end-1):
        while not haystack[start].isalnum() and haystack[start] == needle[start]:
              start += 1
              count = 0
        if(haystack[start].lower() !=  needle[start].lower()):
            count += 1

        start, end = start + 1 , end -1

    return count

print(needleHayStack('hello','ll'))
print(needleHayStack('aaaaa','bba'))
print(needleHayStack('beat','at'))





            



    
    


    