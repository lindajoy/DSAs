my_dictionary = {
    "apple": 10,
    "banana": 5,
    "orange": 7,
    "grape": 12,
    "kiwi": 8
}

        # char_count[char] = char_count.get(char, 0) + 1
# With Python we always have to assign a value, to a particular property we want to change.

my_dictionary["apple"] = my_dictionary.get("apple", 0) + 1
print(my_dictionary)

for i in my_dictionary.keys():
    my_dictionary[i] = my_dictionary.get(i, 0) +10

print("Added by 10", my_dictionary)

my_dictionary["raspberry"] = my_dictionary.get("raspberry", 0) + 1
print('Added raspberry:', my_dictionary)

# This is a better way to approach or add items  on a hashmap
list_one = [(1,), (2,)]  # Convert inner lists to tuples

print(set(list_one))
