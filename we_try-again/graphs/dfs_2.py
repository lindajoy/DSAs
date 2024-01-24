# DFS Implementation 2
# 💡 Iterative approach
def visit():
    pass

marked = [False] * G.size()

def dfs_iter(G, v):
    stack = [v]

    while len(stack) > 0:
        v = stack.pop()

        if not marked[v]:
            marked[v] = True
            visit(v)
            for w in G.neighbours(v):
                if not marked[w]:
                    stack.append(w)

# 💡 Recursive implementation
# I like the idea of recursion: A function calling itself.
# PREORDER
marked = [False] * G.size()

def dfs(G, v):
    visit(v)
    marked[v] = True

    for w in G.neighbours(v):
        if not marked[w]:
            dfs(G, w)

# POSTORDER
            
marked = [False] * G.size()

def dfs(G, v):
    marked[v] = True

    for w in G.neighbours(v):
        if not marked[w]:
            dfs(G, w)
    visit(v)
    