# find pairs in array with target sum

def findPairs(arr, sum):
    numDict = {}
    pairs = []

    for num in arr:
        complement = sum - num
        if complement in numDict:
            pairs.append((complement, num))
            numDict[complement] -= 1
        else:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

    return pairs

nums = list(map(int, input().split()))
target = int(input())

pairs = findPairs(nums, target)

if pairs:
    for pair in pairs:
        print(pair)
else:
    print("No pairs")