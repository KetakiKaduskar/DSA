def trapRainwater(heights):
    lIdx = 0
    rIdx = len(heights)-1
    lMaxHeight = 0
    rMaxHeight = 0
    water = 0

    while(lIdx < rIdx):
        lMaxHeight = max(lMaxHeight, heights[lIdx])
        rMaxHeight = max(rMaxHeight, heights[rIdx])

        if lMaxHeight < rMaxHeight:
            water += lMaxHeight - heights[lIdx]
            lIdx += 1
        else:
            water += rMaxHeight - heights[rIdx]
            rIdx -= 1

    return water

heights = list(map(int, input().split()))
print(trapRainwater(heights))