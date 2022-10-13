"""
Given an array of  integers => sort them: Why would you not use a array.sort()
          Most of the interviews prevent you from using the sort method.
"""

"""
💡 Naive Approach:
     Pseudocode: Declare and intialize the array
                 Loop through the array and select an element
                 The inner loop will be used to compare the slected element from the outer loop with th rest of the elements of the array
                 if any element is less than the selected elements then swap the values
                 Continue this process till entire array is sorted in ascending order
"""

def naive_approach(arr, temp = 0):
   # Sort the array in ascending order
   for i in range(0, len(arr)):
      for j in range(i + 1, len(arr)):
         if(arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
   return(arr)

print(naive_approach([1,2,2,6,7,2]))

# nested loops are dangerous they cause the quadratic time complexity O(N^2)


"""
Use the inbuilt method sorted
"""
prime_numbers = [11,13,7,1,2,3,5]

"""
prime_numbers.sort(reverse=True) => In Descending order
"""

prime_numbers.sort()

print(prime_numbers)


