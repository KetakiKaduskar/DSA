def totalCandies(ranks):
    n = len(ranks)
    l2r = [1 for _ in range(n)]
    r2l = [1 for _ in range(n)]

    for i in range(1, n):
        if ranks[i] > ranks[i - 1]:
            l2r[i] = l2r[i - 1] + 1

    
    for i in range(n - 2, -1, -1):
        if ranks[i] > ranks[i + 1]:
            r2l[i] = r2l[i + 1] + 1

    candies = 0
    for i in range(n):
        candies += max(l2r[i], r2l[i])

    return candies

ranks = list(map(int, input().split()))
print(totalCandies(ranks))