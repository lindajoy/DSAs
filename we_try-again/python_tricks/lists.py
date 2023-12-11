"""
Say you are given a list [a,b,a, c, b,a] and the task is to remove duplicates and maintain the order:
The output for this should be: [a, b, c]
"""
# First implementation would be try out with sets right?
original_list = ["a","b","a", "c", "b","a"]
print(list(set(original_list)))
# Hmm mainatins the order:
# or you can do this:
# From keys converts the original list to keys!
new_list = list(dict.fromkeys(original_list).keys())
print(new_list)