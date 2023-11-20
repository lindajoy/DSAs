"""
🤔 What does this output?
"""
x = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

def foo(m):
    v = m[0][0]
    print("Hello:", v)
    for row in m:
        print("row", row)
        for element in row:
            print("Element", element)
            if v < element:
                v = element
    return v


# print(foo(x[0]))


lst = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
    print(lst[i].pop()),