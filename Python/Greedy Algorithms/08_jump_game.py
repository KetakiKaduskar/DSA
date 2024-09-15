def reachEnd(arr):
    reachable = 0
    for i in range(len(arr)):
        if reachable < i:
            return False
        reachable = max(reachable, i + arr[i])

    return True

arr = list(map(int, input().split()))
print(reachEnd(arr))