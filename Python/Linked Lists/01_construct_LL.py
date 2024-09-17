class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def addToLL(root, val):
#     temp = Node(val)
#     if not root:
#         return temp

#     last = root
#     while last.next is not None:
#         last = last.next
#     last.next = temp
#     return root

# def arrayToLL(arr):
#     root = None  
#     for val in arr:
#         root = addToLL(root, val)
#     return root

def printLL(root):
    while root is not None: 
        print(root.data, end="->") 
        root = root.next

def insert(root, val):
    temp = Node (val)
    temp.next = root
    root = temp
    return root

def arrayToLL(arr):
    root = None 
    for i in range(len(arr) - 1, -1, -1): 
        root = insert(root, arr[i])
    return root

arr = list(input().split())
root = arrayToLL(arr)
printLL(root)