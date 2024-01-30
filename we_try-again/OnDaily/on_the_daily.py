"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression
"""

def resolves(self, a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    return int(a/b)

def evalRPN(tokens):
    stack = []
    for token in tokens:
        # The unicode for 0 is 48, 1 is 49, …., 9 is 57. 
        if len(token) == 1 and ord(token) < 48:
            integer1 = stack.pop()
            integer2 = stack.pop()
            operator = token
            resolved_ans = self.resolves(integer1, integer2, operator)
            stack.append(resolved_ans)
        else:
            stack.append(int(token))
    return stack.pop()


# Come lets see something
print(5 // 2) # Returns 2

# Which is also similar to the operation
# Also returns 2
print(int(5/2))
