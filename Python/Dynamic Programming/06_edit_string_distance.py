def editStringDist(str1, str2):
    numCols = len(str2) + 1
    numRows = len(str1) + 1
    dp = [[0 for _ in range(numCols)] for _ in range(numRows)]

    for i in range(numRows):
        for j in range(numCols):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    
    return dp[numRows - 1][numCols - 1]

str1 = input()
str2 = input()
print(editStringDist(str1, str2))