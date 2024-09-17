def maxSumNonAdjacent(arr):
    include = arr[0]
    exclude = 0

    for i in range(1, len(arr)):
        newInclude = exclude + arr[i]
        newExclude = max(include, exclude)
        include = newInclude
        exclude = newExclude

    return max(include, exclude)

arr = list(map(int, input().split())) 
print(maxSumNonAdjacent(arr))