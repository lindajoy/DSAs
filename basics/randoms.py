string = "Hello, World!"
index = 4
new_char = 'a'

new_string = string[:index] + string[index:].replace(string[index], new_char, 1)

print(new_string)
