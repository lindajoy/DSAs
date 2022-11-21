# Still uses O(n) since it needs to iterate over all elements in the array to get the end list.

def remove_even(list):
    odd = []

    for i  in list:
        if i % 2 != 0:
            odd.append(i)
    return odd

print(remove_even([3, 2, 41, 3, 34]))


# using list comprehensions => Cleaner and more Pythonic way
def remove_even_list(list):
    return [number for number in list if number % 2 !=0]

print(remove_even_list([3, 2, 41, 3, 34]))
