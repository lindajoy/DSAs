# Understanding Default Dict 
"""
Default dict is a subdivision of the dictionary class, Defaultdict is a container like dictionaries, present in the module collection.

The functionality of both dictionaries and defaultdict are almost the same except that defaultdict never raises a keyError.
"""
from collections import defaultdict


dict_one = defaultdict(int)
print(dict_one[3])

"""
Other values that a default dict can have are the following:
  1. Giving a set as the parameter
  2. Giving list as a parameter
"""
# Giving set as the parameter

default_demo = defaultdict(set)

default_demo['one'].add(1)
default_demo['two'].add(2)
default_demo['one'].add(1)
default_demo['three']

print("Here's the default demo:",default_demo)

# Giving list as the parameter

default_demo_list = defaultdict(list)

default_demo_list['four'].append(4)
default_demo_list['four'].append(3)
default_demo_list['five'].append(3)
default_demo_list['six']

print('Here is the demo list', default_demo_list)