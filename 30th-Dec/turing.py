def turing_test(arr):
    """
    Input the array => ["5", "2", "C", "D", "+"]

    Loop through the entire array => If there is 5 append 5
    if there is 2 append 2
    if there is c remove the last value [5]
    if there is D 5*2 = 10
    IF ITS + then do 10 + 10
    """

    # Initialize an empty list
    result = 0

    list_ops = []
    for i in range(len(arr)):

        if arr[i] == "5":
            list_ops.append(5)
        elif arr[i] == "2":
            list_ops.append(2)
        elif arr[i] == "C":
            list_ops.pop()
        elif arr[i] == "D":
            x = list_ops[-1]
            list_ops[-1] = x * 2
        elif arr[i] == "+":
            result = sum(list_ops)

    return result

x = ["5", "2", "C", "D", "+"]
print(turing_test(x))

x[1] = 5
print(x)