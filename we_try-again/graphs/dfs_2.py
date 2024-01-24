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