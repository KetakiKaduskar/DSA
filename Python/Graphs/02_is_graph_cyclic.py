class Node:
    def __init__(self, data): 
        self.data = data 
        self.nbrs = []

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

def isCyclePresent(v, visited): 
    q = [v]

    while q: 
        rem = q.pop(0)

    if visited[rem] == True: 
        return True 
    visited[rem] = True

    for nbr in rem.nbrs:
        if visited[nbr] == False: 
            q.append(nbr)

def isGraphCyclic(graph):
    vtcs = list(graph.keys())
    print(vtcs)
    visited = {graph[key]: False for key in vtcs}

    for v in vtcs:
        if visited[graph[v]] == False:
            cycle = isCyclePresent(graph[v], visited)
            if cycle == True:
                return True

    return False

edges = []
while True:
    edge = input()
    if edge == "":
        break
    u, v = edge.split() 
    edges.append((u, v))

graph, root = constructGraph(edges) 
print(isGraphCyclic(graph))