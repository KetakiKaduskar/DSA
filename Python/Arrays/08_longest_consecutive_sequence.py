arr = list(map(int, input().split()))

dic = {elem: True for elem in arr}

for key in arr:
    if key - 1 in dic:
        dic[key] = False

maxLen = 0
maxStartingPoint = 0
for key in arr:
    if dic[key] == True:
        tempLen = 1
        tempStartingPoint = key

        while tempStartingPoint + tempLen in dic:
            tempLen += 1

        if tempLen > maxLen:
            maxLen = tempLen
            maxStartingPoint = tempStartingPoint

for i in range(maxLen):
    print(maxStartingPoint + i, end=" ")