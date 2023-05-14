def subsequence(array, subsequence):

    sub_start = 0

    for i in array:
        if i == subsequence[sub_start]:
            sub_start += 1

    
        if sub_start == len(subsequence):
            return True

    return False


x = [1,2,3,4,5]
y = [1,2,4]

print(subsequence(x, y))