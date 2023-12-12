list = [1, 2, 3, 4, 5]
list.reverse()
print(list)

# Forgot this 🤔🤣 
random_str = "helloWorld"
reversed_string = random_str[::-1]
print(reversed_string)

string_random = 'helloworld'
reversed_string = ''.join(reversed(string_random))
print(reversed_string)

list.pop(-2)
print(list)

print([0] * 10)

# List concatenation 

print([1, 2, 3] + [0] * 3)

# Instantiate a 2D Array
d_array = [[1,2,4], [3,5,7,9], [13,14,15]]
print(d_array[1][2])
print(d_array[0][1])

# Checking if a value is present in an array using in array
names = ["Joy", "Lidah", "Ann", "Rita", "Mwenda", "Justin"]

# This operation takes O(n) time.
print("Joy" in names)
print('Anne' in names)

# Key methods in list
random_numbers = [53, 27, 64, 33, 49, 21, 58, 42, 67, 25]
print(max(random_numbers))
print(min(random_numbers))
print(random_numbers.reverse())
print(reversed(random_numbers))
print(random_numbers.sort())
print(sorted(random_numbers))
print(random_numbers[1:4] )
del random_numbers[1:7]
print(random_numbers)