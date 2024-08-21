#find subarray with max sum

def kadanes(arr):
    
    if all(num < 0 for num in arr):
        return max(arr), [max(arr)]
    
    csum = arr[0]
    osum = arr[0]
    cans = [arr[0], ]
    oans = [arr[0], ]

    for i in range(1, len(arr)):
        if csum < 0:
            cans.clear()
            cans.append(arr[i])
            csum = arr[i]
        else:
            cans.append(arr[i])
            csum += arr[i]

        if osum < csum:
            oans = cans[:]
            osum = csum

    return osum, oans

arr = list(map(int, input().split()))
osum, oans = kadanes(arr)
print(osum)
print(oans)