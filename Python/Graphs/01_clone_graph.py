# import copy

class Node:

    def __init__(self, val):
        self.val = val
        self.nbrs = []

    def __repr__(self):
        return f"Node({self.val})"

def constructGraph(edgeList):
    nodes = {}

    for u, v in edgeList:
        if u not in nodes:
            nodes[u] = Node(u) 
        if v not in nodes:
            nodes[v] = Node(v)

        nodes[u].nbrs.append(nodes[v])
        nodes[v].nbrs.append(nodes[u])

    return nodes, nodes[edgeList[0][0]]

def printGraph(root):
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        print(node.val, end=" ")

        for nbr in node.nbrs:
            dfs(nbr)

    dfs(root)

def cloneGraph(root):
    clonedNodes = {}

    def dfs(node):
        if node in clonedNodes:
            return clonedNodes[node]

        clonedNode = Node(node.val)
        clonedNodes[node] = clonedNode

        for nbr in node.nbrs:
            clonedNode.nbrs.append(dfs(nbr))

        return clonedNode

    return dfs(root)

edges = []
while True:
    inp = input().strip()
    if inp == "":
        break
    u, v = inp.split()
    edges.append((u, v))

graph, root = constructGraph(edges)

print("og:")
printGraph(root)
print("\n")

clonedRoot = cloneGraph(root)
# clonedRoot = copy.deepcopy(root)
print("cg:")
printGraph(clonedRoot)