class Edge:
    def __init__(self, src, nbr, wt):
        self.src = src
        self.nbr = nbr
        self.wt = wt

class Pair:
    def __init__(self, node, psf, wsf):
        self.node = node
        self.psf = psf
        self.wsf = wsf

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def add(self, data):
        self.pq.append(data)

    def remove(self):
        self.pq.sort(key=lambda x: x.wsf)
        return self.pq.pop(0)
    
    def size(self):
        return len(self.pq)

def shortestPathByWt(graph, src, dest):
    pq = PriorityQueue()
    pq.add(Pair(src, str(src), 0))
    visited = [False for _ in range(vtcs)]

    while pq.size() > 0:
        rem = pq.remove()
        if visited[rem.node] == True:
            continue

        visited[rem.node] = True

        if rem.node == dest:
            break

        for edge in graph[rem.node]:
            if visited[edge.nbr] == False:
                pq.add(Pair(edge.nbr, rem.psf + str(edge.nbr), rem.wsf + edge.wt)) 

    return rem.psf, rem.wsf

vtcs = int(input())
graph = [[] for _ in range(vtcs)]
while True:
    inp = input()
    if inp == "":
        break
    v1, v2, wt = map(int, inp.split())
    graph[v1].append(Edge(v1, v2, wt))
    graph[v2].append(Edge(v2, v1, wt))

src = int(input())
dest = int(input())
print(shortestPathByWt(graph, src, dest))