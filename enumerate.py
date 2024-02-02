"""
Understanding the enumerate function in Python list

list = 2,7,11,15
ENUMERATE function allows you to print out indexes and the associated numbers
"""


list_one = [2,7,11, 15]
sample_list = [(nums, idx) for nums, idx in enumerate(list_one)]

print("😁", sample_list)

sample_list2 = [(nums, idx) for idx, nums in enumerate(list_one)]
print('😁❌', sample_list2)

stringA = 'cc'
stringB = 'bb'

def linear_merge(list1, list2):
    if len(list1) == 0 and len(list2) == 0:
        return []
    if len(list1) == 0:
        return list1
    if len(list2) == 0:
        return list2
    merged_list = []
    ptrListOne, ptrListTwo = 0, 0
    while ptrListOne < len(list1) and ptrListTwo < len(list2):
        if list1[ptrListOne] < list2[ptrListTwo]:
            merged_list.append(list1[ptrListOne])
            ptrListOne += 1
        elif list1[ptrListOne] > list2[ptrListTwo]:
             merged_list.append(list2[ptrListTwo])
             ptrListTwo += 1
        # else:
        #     merged_list.append(list2[ptrListTwo])
        #     merged_list.append(list1[ptrListOne])
        #     ptrListTwo += 1
        #     ptrListOne += 1
    if ptrListTwo < len(list2) - 1:
        other_part = list2[ptrListTwo:]
        merged_list = merged_list.extend(other_part)
    elif ptrListOne < len(list1) - 1:
        other_part = list1[ptrListOne:]
        merged_list = merged_list.extend(other_part)
    return merged_list

print(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']))