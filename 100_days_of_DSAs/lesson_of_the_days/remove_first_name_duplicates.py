"""
REMOVE FIRST NAME DUPLICATES 

Design an efficient algorithm for removing all first-name duplicates from an array.
For exam- ple, if the input is ((Ian,Botham),(David,Gower),(Ian,Bell),(Ian,Chappell)), one result could be ((Ian, Bell), (David, Gower));
((David, Gower), (Ian, Botham)) would also be acceptable.

"""
names = [['Ian','Botham'], ['David','Gower'], ['Ian','Bell'], ['Ian','Chappell']]
# print(sorted(names, key=lambda x: x[0]))
def remove_duplicates(arr):
    sorted_names = sorted(arr, key=lambda x: x[0])
    # print(sorted_names)
    without_duplicates = []
    left = 0
    right = left + 1

    while right <= len(arr) - 1:
        if sorted_names[left][0] == sorted_names[right][0]:
            without_duplicates.append(sorted_names[left])
            right += 1
        else:
            without_duplicates.append(sorted_names[left])
            left = right
            right = right + 1

    without_duplicates.append(sorted_names[left])
    without_duplicates_tuples = [tuple(item) for item in without_duplicates]
    without_duplicates_set = set(without_duplicates_tuples)
    return without_duplicates_set

print(remove_duplicates(names))

names2 =  [("John", "Smith"), ("Jane", "Doe"), ("John", "Smith"), ("Adam", "Johnson")]
print(remove_duplicates(names2))
    
