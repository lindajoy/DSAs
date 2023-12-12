"""
List comprehensions:   
    => Provides a concise way to create lists.
    => Common applications are to make new lists where each element is the result of some operation applied to each member of another sequence or iterable or to create 
        subsequence of those elements that satisty a certain condition.
"""

# Random 

squares = []
for x in range(10):
    squares.append(x**2)

print("Squares 1", squares)

# Or we can do:
squares_2 = list(map(lambda x: x**2, range(10)))
print(squares_2)

# or, equivantely:
squares_3 = [x**2 for x in range(10)]
print(squares_3)

# List comprehension syntax: 
# newList = [expression for item in iterable if condition == True]
names = ["Joy", "Lidah", "Ann", "Rita", "Mwenda", "Justin"]

new_names =[name for name in names if 'J' in name]
print('New Names 😮‍💨:', new_names)
formatted_names = [name.lower() for name in names]
print("Formatted names:",formatted_names)
formatted_names2 = [name.upper() for name in names]
print("Formatted names:",formatted_names2)

name = "Chris"

if name in ["Bob" , "Tom" , "Mike"]:
    print("Access Granted!")
else:
    print("Access Denied!")

# 💡 Really Interesting Bit: Very Interesting
num1 = 1_000_000_000
num2 = 4_000
ans = num1 *num2
print(f'{ans:,}')

