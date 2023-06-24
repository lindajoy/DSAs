"""
Pass By Value vs Pass By Reference

In pass by value, the value of a function parameter is copied to another location of the memory.
When accessing or modifying the variable within the function, it accesses only the copy. 
Thus, there is no effect on the original value.

In pass by reference, the memory address is passed to that function. 
In other words, the function gets access to the actual variable.
"""

# 💡 Pass By Value
my_variable1 = 'Joy' 

my_name1 = my_variable1
print(my_name1)

my_name1 = "Joy Linda"
print(my_name1)
print(my_variable1)

# 💡 Pass By Reference

my_variable2 = "Wawira"

def print_my_name(name):
    return name

print(print_my_name(my_variable2))