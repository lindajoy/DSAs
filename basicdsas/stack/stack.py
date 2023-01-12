"""
Stack Data Structure
"""

class Stack():
    def __init__(self):
        # The constructor initializes an Empty Python list.
        self.items = []

    # Push is a member of this class and takes item as argument.
    def push(self, item):
        # append adds items at the end of the list.
        self.items.append(item)

    # Pop returns the last inserted value on the list.
    def pop(self):
        return self.items.pop()

    '''
    💡 Trying out the insertion function that allows one to insert an element at a specific index.
    Wanted to test this out to see which element would be popped out of the list.
    '''
    # def insert_2(self,item):
    #     return self.items.insert(0, item)

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


myStack = Stack()
myStack.push("A")
myStack.push("B")
# myStack.insert_2("D")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
    

    
my_simple_list = [1,2,3,4,5,6]
my_simple_list.append(3)
print(my_simple_list)