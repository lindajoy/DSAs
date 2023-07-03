"""
A company is planning to interview 2n people. 
Given the array costs where costs[i] = [aCosti, bCosti], 
the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""

costs = [[10,20],[30,200],[400,50],[30,20]]

def twoCityScheduling(travelcosts:list[int]):
    # Initialize total costs to zero
    totalCost = 0

    # Get the length of the travel costs
    lengthofList = len(travelcosts) // 2
    # Sort the list by ascending order based on the difference
    travelcosts.sort(key= lambda x: x[0] - x[1])


    # First Two Array
    firstHalf = travelcosts[:lengthofList]
    SecondHalf= travelcosts[lengthofList:]

    totalCost = sum([i[0] for i in firstHalf]) + sum([i[1] for i in SecondHalf])
    
    # for i in firstHalf:
    #     totalCost += i[0]

    # for i in SecondHalf:
    #     totalCost += i[1]

    
    return totalCost

#  total_cost = sum([i[0] for i in first_half]) + sum([i[1] for i in second_half])

print(twoCityScheduling(costs))