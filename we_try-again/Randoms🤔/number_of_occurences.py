"""
Unique Number of Occurrences

Given an array of integers arr, 
return true if the number of occurrences of each value in the array is unique or false otherwise.


"""
def uniqueOccurrences(arr):
        count_dict = {}
        count_set = set()

        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        occurences = [value for value in count_dict.values()]

        for occ in occurences:
            if occ in count_set:
                return False
            else:
                count_set.add(occ)
        return True
     
        
        