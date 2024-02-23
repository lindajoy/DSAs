"""
CHEAPEST FLIGHTS WITHIN K STOPS.

There are n cities connected by some number of flights. 
You are given an array flights where flights[i] = [from(i), to(i), price(i)]
indicates that there is a flight from city from(i) to city to(i) with cost price(i)

You are also given three integers src, dst and k, return the cheapest price 
from src to dst with at most k stops. If there is no such route, return -1
"""
# Intuition: This means that the stops can be equal or less than k.

"""
Input:
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
"""

# My Initial thought was using a Breadth First Algorithm first => This was what was going through my head when I saw this question.
# Actually you can use a BFS for this question.🤔

# First question: How Does a Bfs work?

# With BFS, say we have a graph it goes level on level iterating and getting all its neighbours while we ae still on the same level.

# So in this case: What are we doing?

from collections import defaultdict, deque

# Hmm this is an interesting way of doing this..🤔
"""
    @params
    n is the number of cities
    flights is an array of flights where flightsi(i)
"""
# Whenever it comes to queues; The first thing we should always think about is":
# Queues?
# How do queues work?
#
# Queues flow the the principle of First In, First Out Principle.
# You can picture a line in a coffee shop, the first customer to get a coffee from starbucks will get attended first.
# Hmm, needs more perspective: 🤔

def findCheapestPrice(n, flights, src, dst, K):
    # Here we are saving all the neighbours in an adjacency list 
    adj = defaultdict(list)
    # Initialize the visited array to the n
    # So we will have to have something like this: In the case where n = 4
    # [inf, inf, inf, inf]
    visited = [float('inf')] * n
    # We initialize the src to 0 since at this point we have not used any amount of money yet
    visited[src] = 0

    for flight in flights:
        # Here we are appending the  destination and k
        adj[flight[0]].append((flight[1], flight[2]))
    
    # [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    # 0: [(1, 100)], 1: [(2, 100), (3, 600)], 2: [(0, 100), (3, 200)]
    print(adj)
    queue = deque([(src, 0)])
    K += 1

    while K > 0 and queue:
        size = len(queue)
        while size > 0:
            curr_node, curr_price = queue.popleft()
            for neighbor, price in adj[curr_node]:
                print(neighbor, price)
                new_price = curr_price + price
                if new_price < visited[neighbor]:
                    visited[neighbor] = new_price
                    queue.append((neighbor, new_price))

            size -= 1
        K -= 1

    return visited[dst] if visited[dst] != float('inf') else - 1

n = 4 
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 2
print(findCheapestPrice(n, flights,src, dst, k))

n2 = 3
flights2 = [[0,1,100],[1,2,100],[0,2,500]]
src2 = 0
dst2 = 2
k2 = 0
print(findCheapestPrice(n2, flights2,src2, dst2, k2))




# In this question we use the Bell-Man Ford Shortest Algorithm. 
