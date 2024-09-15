def lengthLPS(str):
    n = len(str)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(n):
        i = 0
        for j in range(gap, n):
            if gap == 0:
                dp[i][j] = 1
            elif gap == 1:
                print(i, j, str[i], str[j])
                if str[i] == str[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1
            else:
                if str[i] == str[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            i += 1

    print(dp)
    return dp[0][n - 1]

string = input()
print(lengthLPS(string))