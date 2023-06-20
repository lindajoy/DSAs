"""
Dictionaries vs defaultDict
"""
dict_demo = dict()
# dict_demo[3] = "k"
# print(dict_demo)
dict_demo['Kenya'] = 'Nairobi'
dict_demo['Uganda'] = "Kampala"
dict_demo['Tanzania'] = "Dodoma"
print(dict_demo)

# Introducing the default dict data structure
from collections import defaultdict

defaultdict_demo = defaultdict(int)
print(defaultdict_demo[3])

defaultdict_demo2 = defaultdict(set)
defaultdict_demo2['one'].add(1)
defaultdict_demo2['two'].add(2)
defaultdict_demo2['three'].add(3)
print(defaultdict_demo2)


defaultdict_list = defaultdict(list)
defaultdict_list['one'].append(1)
defaultdict_list['one'].append(2)
defaultdict_list['two'].append(3)
print(defaultdict_list)