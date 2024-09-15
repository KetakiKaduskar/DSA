heights = list(map(int, input().split()))

lIdx = 0
rIdx = len(heights) - 1
ans = 0

while lIdx < rIdx:

    height = min(heights [lIdx], heights [rIdx])
    width = rIdx - lIdx
    water = height * width
    ans = max(ans, water)

    if heights[lIdx] < heights [rIdx]: 
        lIdx += 1
    else:
        rIdx -= 1

print(ans)