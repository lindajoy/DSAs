"""
In this problem, you have to implement the find_sum(lst,k) 
function which will take a number k as input and return two numbers that add up to k.

Input
A list and a number k

Output
A list with two integers a and b that add up to k

Sample Input
lst = [1,21,3,14,5,60,7,6]
k = 81
"""
"""
🧮 Longer method
"""
"""
The time complexity here is 0(n) since we are looping through each element in the entire array
"""
lst = [1,21,3,14,5,60,7,6]
k = 81

def find_two_sum_k(lst, k):
    for i in range(len(lst)):
        remainder = k - lst[i]
        if remainder in lst:
            return [lst[i], remainder]
  
print(find_two_sum_k(lst, k))

"""
Method 2: Using a Set 😊
"""
def find_two_sum(lst, k):
    # Sets dont contain  duplicates.
    result = set()
    print('Here is the result:', result)
    for i in lst:
        if i in result:
            return [i, k-i]
        result.add(k-i)

print(find_two_sum(lst,k))