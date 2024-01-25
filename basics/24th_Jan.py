# I dont think I knew this 🤔
random_str = 'abc'
print('Hello My random List:', list(random_str))

random_str_with_spaces = "Joy is hustling"
print('Splitting a string with spaces:', random_str_with_spaces.split())

random_str_with_commas = "Yellow, blue, red, white, red, white, red, white, gray, blue, red, white,  white, white, white"
print('Splitting with comma:', random_str_with_commas.split(','))
list_one =  [1, 2, 3, 4, 5, 6, 8, 9, 1, 2, 3, 4, 5, 6, 8, 9, 1, 2, 3, 4, 5, 6, 8, 9]

from collections import Counter
count = Counter(list_one)

for i in range(10):
    print ('Hey here is my count:','for',i, 'the count is', count[i])


my_empty_dictionary = {}

# Create the dictionary!
for i in list_one:
    my_empty_dictionary[i] = my_empty_dictionary.get(i, 0) + 1
    
for i in range(10):
    if i in my_empty_dictionary:
        print("My Empty Dictionary", my_empty_dictionary[i])
    else:
        print(i, 'does not exist')

# Slicing lets work with lists today
rnb_singers = [
    "Beyoncé",
    "Drake",
    "Rihanna",
    "Bruno Mars",
    "The Weeknd",
    "Alicia Keys",
    "John Legend",
    "Chris Brown",
    "Khalid",
    "Janelle Monáe",
    "Summer Walker",
    "Redd"
]

print('Slicing',rnb_singers[2:-2])
summer_walker = rnb_singers[-2]
summer_walker = summer_walker.replace(" ", "")
print('Got Summer walker:', summer_walker)
print(summer_walker[7:])
print(summer_walker.lower())
print(summer_walker.upper())
print(summer_walker.title())

# A string is an iterable:
# So you can do this:

for i in summer_walker:
    print(i)

for i in range(len(summer_walker)):
    print(summer_walker[i])



    




