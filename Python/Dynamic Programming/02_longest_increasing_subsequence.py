def longestIncreasing(arr): 
    n = len(arr) 
    dp = [0 for _ in range(n)] 
    omax = 0

    for i in range(n): 
        tmax = 0 
        for j in range(i): 
            if arr[j] < arr[i]: 
                tmax = max(tmax, dp[j]) 
        dp[i] = tmax + 1 
        omax = max(omax, dp[i])

    return omax

arr = list(map(int, input().split()))
print(longestIncreasing(arr))