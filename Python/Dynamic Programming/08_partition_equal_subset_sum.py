def equalSumSubsets(arr, idx, k, ans, subsetSum, numOfSubsets):

    if len(arr) < k:
        print("-1")
        return
    
    if sum(arr) % k != 0:
        print("-1")
        return

    if numOfSubsets == k and sum(len(subset) for subset in ans) == len(arr):
        if all(subsetSum[i] == subsetSum[0] for i in range(k)):
            print(*ans)
            return

    for j in range(k):
        if len(ans[j]) and idx < len(arr):
            ans[j].append(arr[idx])
            subsetSum[j] += arr[idx]
            equalSumSubsets(arr, idx + 1, k, ans, subsetSum, numOfSubsets)
            subsetSum[j] -= arr[idx]
            ans[j].pop()
        elif idx < len(arr):
            ans[j].append(arr[idx])
            subsetSum[j] += arr[idx]
            equalSumSubsets(arr, idx + 1, k, ans, subsetSum, numOfSubsets + 1)
            subsetSum[j] -= arr[idx]
            ans[j].pop()
            break

arr = list(map(int, input().split()))
k = int(input())

ans = [[] for _ in range(k)]
subsetSum = [0 for _ in range(k)]
numOfSubsets = 0

equalSumSubsets(arr, 0, k, ans, subsetSum, numOfSubsets)