def minPlatforms(arr, dep):
    n = len(arr)
    
    arr.sort()
    dep.sort()
    i = 0
    j = 0
    maxTrains = 0
    platforms = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:
            maxTrains += 1
            i += 1
        else:
            maxTrains -= 1
            j += 1
        platforms = max(platforms, maxTrains)

    return platforms

arrivals = list(map(int, input().split()))
depatures = list(map(int, input().split()))
print(minPlatforms(arrivals, depatures))