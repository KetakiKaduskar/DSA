class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt

class Pair:
    def __init__(self, v, av, wt):
        self.v = v
        self.av = av
        self.wt = wt

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def size(self):
        return len(self.pq)
    
    def add(self, data):
        self.pq.append(data)

    def remove(self):
        self.pq.sort(key=lambda x: x.wt)
        return self.pq.pop(0)
    
def prims(graph):
    pq = PriorityQueue()
    pq.add(Pair(0, -1, 0))
    visited = [False for _ in range(vtcs)]

    totalWire = 0
    while pq.size() > 0:
        rem = pq.remove()

        if visited[rem.v] == True:
            continue
        visited[rem.v] = True

        print(rem.v, rem.av, rem.wt)
        totalWire += rem.wt
        for edge in graph[rem.v]:
            if visited[edge.nbr] == False:
                pq.add(Pair(edge.nbr, rem.v, edge.wt))

    return totalWire

vtcs = int(input())
graph = [[] for _ in range(vtcs)]
while True:
    inp = input()
    if inp == "":
        break
    v1, v2, wt = map(int, inp.split())
    graph[v1].append(Edge(v1, v2, wt))
    graph[v2].append(Edge(v2, v1, wt))

print(prims(graph))