def longestMountain(arr):
    # Initialize answer and index i
    ans = 0
    i = 0

    # loop through the array
    for i in range(len(arr) - 1):
        # Hmm, I really dont like repeating this line: i + 1 < len(arr)
        while i + 1 < len(arr) and arr[i] == arr[i+1]:
            i+=1
        increasing = 0
        decreasing = 0

        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            increasing += 1
            i += 1

        while i + 1 < len(arr) and arr[i] > arr[i + 1]:
            decreasing += 1
            i += 1

        if increasing > 0 and decreasing > 0:
            ans = max(ans, increasing + decreasing + 1)

    return ans

print(longestMountain([2,1,4,7,3,2,5]))