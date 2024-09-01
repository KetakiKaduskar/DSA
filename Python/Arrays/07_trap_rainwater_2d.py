class Pair:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append(data)

    def size(self):
        return len(self.queue)

    def remove(self):
        self.queue = sorted(self.queue, key=lambda x: x.height)
        return self.queue.pop(0)

def trapRainwater(matrix):
    
    m = len(matrix)
    n = len(matrix[0])
    
    pq = PriorityQueue()
    vis = [[False for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                pq.add(Pair(i, j, matrix[i][j]))
                vis[i][j] = True

    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    water = 0

    while pq.size() > 0:
        rem = pq.remove()

        for dir in dirs:
            rowDash = rem.row + dir[0]
            colDash = rem.col + dir[1]

            if rowDash >= 0 and rowDash < m and colDash >= 0 and colDash < n and vis[rowDash][colDash] == False:
                water += max(0, rem.height - matrix[rowDash][colDash])

                if matrix[rowDash][colDash] >= rem.height:
                    pq.add(Pair(rowDash, colDash, matrix[rowDash][colDash]))
                else:
                    pq.add(Pair(rowDash, colDash, rem.height))

                vis[rowDash][colDash] = True

    return water

matrix = []
while True:
    row = input().strip()
    if not row:
        break
    matrix.append(list(map(int, row.split())))

print(trapRainwater(matrix))