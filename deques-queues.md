# Python's deque: Implement Efficient Queues and Stacks

Queues follows the first in first out principle, meaning the first element in is the first element out while deque follows the last in first out principle => Elements can be added or removed from both ends of the deque.

Deque is provided in the *collections* module, Offers methods like "append()" to add an element at the right end, "appendleft()" to add an element on the left end, "pop" to remove the element from the right hand, and "popleft" to remove an element from the left end

# Use cases:
Queue are commonly used for managing tasks in a multi-threaded or multi-process environment, where different threads or processes can enqueue and dequeue items in a coordinated manner.

Deques are useful in scenarios where you need effecient insertion and deletion of both elements at both ends of the collection.

Can be used to implement algorithms like breadth search first, maintaing a sliding window, window of elements etc.