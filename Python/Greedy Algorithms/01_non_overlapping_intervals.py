def nonOverlapping(starts, ends):
    a = []
    for i in range(len(starts)):
        a.append([i+1, starts[i], ends[i]])
    a.sort(key=lambda x: x[2])

    ans = []
    ans.append(a[0][0])

    for i in range(0, len(a) - 1):
        print(a[i + 1], a[ans[-1] - 1])
        if a[i + 1][1] > a[ans[-1] - 1][2]:
            ans.append(a[i + 1][0])

    return ans

starts = list(map(int, input().split()))
ends = list(map(int, input().split()))
print(nonOverlapping(starts, ends))