def coinChange(coins, amt):
    dp = [0 for _ in range(amt + 1)]
    dp[0] = 1

    for val in coins:
        for j in range(val, len(dp)):
            dp[j] += dp[j - val]

    return dp[amt]

coins = list(map(int, input().split()))
amt = int(input())
print(coinChange (coins, amt))