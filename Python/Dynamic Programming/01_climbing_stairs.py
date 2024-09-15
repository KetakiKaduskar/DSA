def countPaths(n, dp):
    if n < 0 :
        return 0
    if n == 0 or n ==1 :
        return 1

    if dp[n] > 0:
        return dp[n]

    cp1 = countPaths(n - 1, dp)
    cp2 = countPaths(n - 2, dp)
    cp3 = countPaths(n - 3, dp)

    return cp1+cp2+cp3

# def countPaths (n): 
#     dp = [0 for _ in range(n + 1)]
#     dp[0] = 1
    
#     for i in range(1, n+1):
#         if i == 1:
#             dp[i] = dp[i - 1]
#         elif i == 2:
#             dp[i] = dp[i - 1] + dp[i - 2]
#         else:
#             dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

#     return dp[n]

n = int(input())
dp = [0 for _ in range(n + 1)]
print(countPaths(n, dp))