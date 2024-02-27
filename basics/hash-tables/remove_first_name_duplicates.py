"""
REMOVE FIRST NAME DUPLICATES.

Design an efficient algorithm for removing all first-name duplicates from an array.
For example, 
if the input is ((Ian,Botham),(David,Gower),(Ian,Bell),(Ian,Chappell)), 
one result could be ((Ian, Bell), (David, Gower)); ((David, Gower), (Ian, Botham)) would also be acceptable.

"""
# Used the left and right pointer for this solution

names2 =[('Ian','Botham'),('David','Gower'),('Ian','Bell'),('Ian','Chappell')]

def remove_first_name_duplicates(names):
    sorted_names = sorted(names, key = lambda x: x[0])
    left, right = 0, 1

    while right < len(sorted_names):
        if sorted_names[left][0] != sorted_names[right][0]:
            left += 1
            right += 1
        elif sorted_names[left][0] == sorted_names[right][0]:
            sorted_names.pop(right)
            right = left + 1
    return sorted_names

print(remove_first_name_duplicates(names2))