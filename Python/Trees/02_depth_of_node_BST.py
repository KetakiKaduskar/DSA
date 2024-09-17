class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

def constructBST(arr):
    root = None 
    for data in arr: 
        root = insert(root, data)
    return root

# def constructBST(arr, lo, hi):
#     if lo > hi:
#         return None

#     mid = (lo + hi) // 2
#     data = arr[mid]

#     leftChild = constructBST(arr, lo, mid - 1) 
#     rightChild = constructBST(arr, mid + 1, hi)

#     node = Node(data, leftChild, rightChild)
#     return node

def depthOfNode(root, data, count):
    if root == None:
        return [-1]

    count[0] += 1
    if root.data > data:
        count = depthOfNode(root.left, data, count)
    elif root.data< data:
        count = depthOfNode(root.right, data, count)
    else:
        return count

    return count

arr = list(map(int, input().split()))
# arr.sort()
# root = constructBST(arr, 0, len(arr) - 1)
root = constructBST(arr)
depth = depthOfNode(root, 8, [0])
print(depth[0])