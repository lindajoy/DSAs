def needleHayStack(haystack,needle):
    start, end = 0, len(haystack) - 1
    count = 0

    # Get rid of the case, where the needle does not exist in the haystack
    if needle not in haystack:
        return -1

    while start < end:
        while not haystack[start].isalnum() and haystack[start] == needle[start]:
            start += 1
            count = 0

        if haystack[start].lower()  != needle[start].lower():
            count += 1

        start, end = start + 1, end - 1
    return count


# testing out..

x = 'needle'
y = 'le'

print(x.index(y))
