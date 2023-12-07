def binary_search(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        mid = (start+end) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    
    return -1

print(binary_search([1,2,3,4,5], 1))