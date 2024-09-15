def uniquePaths(srcRow, srcCol, destRow, destCol, dp):
    
    if dp[(srcRow, srcCol)]:
        return dp[(srcRow, srcCol)]
    
    if srcRow == destRow and srcCol == destCol:
        bres = []
        bres.append("")
        return bres

    if srcRow < destRow:
        vPaths = uniquePaths(srcRow + 1, srcCol, destRow, destCol, dp)
    
    if srcCol < destCol:
        hPaths = uniquePaths(srcRow, srcCol + 1, destRow, destCol, dp)
    
    paths = []

    try:
        for hPath in hPaths:
            paths.append("h" + hPath)
    except UnboundLocalError:
        pass

    try:
        for vPath in vPaths:
            paths.append("v" + vPath)
    except UnboundLocalError:
        pass

    dp[(srcRow, srcCol)] = paths

    return paths

srcRow, srcCol, destRow, destCol = map(int, input().split())

dp = {}
for i in range(srcRow, destRow + 1):
    for j in range(srcCol, destCol + 1):
        key = (i, j)
        value = None
        dp[key] = value

print(uniquePaths(srcRow, srcCol, destRow, destCol, dp))