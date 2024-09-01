arr = list(input().split())
k = int(input())

k = k % len(arr)

p1 = arr[:len(arr)-k]
p2 = arr[len(arr)-k:]

p1 = p1[::-1]
arr[:len(arr)-k] = p1

p2 = p2[::-1]
arr[len(arr)-k:] = p2

arr = arr[::-1]

print(arr)