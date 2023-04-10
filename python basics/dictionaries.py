# Creating / Initializing a dictionary can be done in two ways
dict_one = dict()
dict_two = {}

# Populating the dictionary
# 💡 METHOD 1

dict_two["name"] = "Joy Lidah Wawira"
print(dict_two)

# 💡 METHOD 2
dict_one = {"name", "Kekeli Oluoch"}
print(dict_one)

# 💡 METHOD 3 => KeyWord argument list
dict_three = dict(age = "21", month = "July")
print(dict_two)

# PYTHON DICTIONARY METHODS.

# Update Function

harry_potter_chars = {
    "Harry Potter" : "Gryfindor",
    "Albus Dumbledore": "Gryfindor",
    "Cedric Malfoy" : "Slytherin"
}
print('😫',harry_potter_chars)

another_set_of_harry_potter_chars = {
    "Helena RavenClaw": "RavenClaw",
    "Hermoinine Granger" : "Gryfindor",
}

print('😇', another_set_of_harry_potter_chars)


merged_dict = harry_potter_chars.update(another_set_of_harry_potter_chars)

print('❌', merged_dict)
