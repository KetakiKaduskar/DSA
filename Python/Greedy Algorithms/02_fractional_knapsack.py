def maxTotalVal(wts, vals, cap):
    
    n = len(wts)
    ratios = []
    for i in range(n):
        ratios.append([vals[i]/wts[i], i])
    
    ratios.sort(key=lambda x: x[0], reverse=True)

    ans = 0
    
    for i in range(len(ratios)):
        idx = ratios[i][1]

        if cap >= wts[idx]:
            cap -= wts[idx]
            ans += vals[idx]
        else:
            frationVal = cap * vals[idx] / wts[idx]
            ans += frationVal
            break

    return ans

wts = list(map(int, input().split()))
vals = list(map(int, input().split()))
cap = int(input())

print(maxTotalVal(wts, vals, cap))