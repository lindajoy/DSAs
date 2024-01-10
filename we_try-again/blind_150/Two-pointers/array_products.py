"""
Write a function that takes in a non-empty array of integers and returns an array of the same length,
where each element in the output array is equal to the product of every other number in the input array.

In other words, the value at output[i] is equal to the product of every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
"""

array = [5, 1, 4, 2]
output =[8, 40, 10, 20]

# 💡 A reminder on slicing.
print('Sliced at index 1',array[1:])
print('sliced at index 2' ,array[2:]+ array[:1])

def arrayOfProducts(nums):
    n = [0] * len(nums)

    def calc_product(index, list):
        product = 1
        for i in list:
            product *= i
        n[index] = product

    for i in range(len(nums)):
        if i == 0:
            concat_list = nums[1:]
            calc_product(i, concat_list)
        else:
            concat_list2 = nums[i+1:] + nums[:i]
            calc_product(i, concat_list2)
    return n


print(arrayOfProducts(array))
print(arrayOfProducts([1, 2, 0, 4]))
print(arrayOfProducts([-1, 2, -3, 4]))
print(arrayOfProducts([2, -3, 4, -5]))


# Lets do some slicing revision:
frodo_characters = [
    "Bilbo Baggins", #0
    "Samwise Gamgee", #1
    "Frodo Baggins", #2
    "Peregrin Took (Pippin)", #3
    "Meriadoc Brandybuck (Merry)", #4
    "Gandalf", #5
    "Aragorn", #6
    "Legolas", #7
    "Gimli", #8
    "Thorin Oakenshield"#9
]

print(frodo_characters[:2]) # ['Bilbo Baggins', 'Samwise Gamgee']
print(frodo_characters[2:]) #['Frodo Baggins', 'Peregrin Took (Pippin)', 'Meriadoc Brandybuck (Merry)', 'Gandalf', 'Aragorn', 'Legolas', 'Gimli', 'Thorin Oakenshield']
# Something to note here is that before frodo baggins is being printed on the list else we only have Bilbo and Samwise.

# 🍰 Slicing syntax has the notation lst[start:end:stop]
# Reversing frodo_characters using slice notation.
print(frodo_characters[::-1])
# Prints all the names that index%2 == 0
print('We wanna see something here..',frodo_characters[::2])
print('Slicing from index 5 to 8', frodo_characters[5:8])
print('slicing from index 6 till the end,', frodo_characters[6:])