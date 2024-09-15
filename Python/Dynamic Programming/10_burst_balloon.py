def maxAmount(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(n):
        i = 0
        mx = 0
        for j in range(gap, n):
            for k in range(i, j + 1):
                left = 0 if i == k else dp[i][k - 1]
                right = 0 if j == k else dp[k + 1][j]
                val = (1 if i == 0 else arr[i - 1]) * arr[k] * (1 if j == n - 1 else arr[j + 1])

                total = left + right + val

                if total > mx:
                    mx = total

            dp[i][j] = mx
            i += 1

    return dp[0][n - 1]

arr = list(map(int, input().split()))
print(maxAmount(arr))