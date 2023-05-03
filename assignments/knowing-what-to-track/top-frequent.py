def count_most_frequent(nums, k):
    # Initialize an empty dictionary
    count_nums = {}
    # Initialize an empty list
    k_frequent = []

    # Loop through the entire list
    for i in range(len(nums)):
        if i in count_nums:
            count_nums[i] += 1
        else:
            count_nums[i] = 1

    # Loop through the dictionary
    for key,value in count_nums.items():
        print(key, ':', value)

#print(count_most_frequent([1,1,2,2,2,3], 2))

#  Solution 2 => This is the optimal solution
def topKfrequent(nums: list[int], k:int):
    # intialize an empty dictionary
    count = {}
    # List
    freq =[[] for i in range(len(nums) + 1)]
    print('😁', freq)

    for n in nums:
        print(n)
        count[n] = 1 + count.get(n, 0)
    # Loop through the dictionary
    for n, c in count.items():
        freq(c).append(n)

    # Initialize an empty array
    res = []

    for i in range(len(freq) -1, 0, -1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res

print(topKfrequent([1,1,2,3,3,3,4,5,6,5,6,6,], 3))
    