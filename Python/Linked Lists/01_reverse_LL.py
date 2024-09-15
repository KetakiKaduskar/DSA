class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(root):
    while root is not None:
        print(root.data, end="->")
        root = root.next

def insert(root, val):
    temp = Node(val)
    temp.next = root
    root = temp
    return root

def arrayToLL(arr):
    root = None
    for i in range(len(arr) - 1, -1, -1):
        root = insert(root, arr[i])

    return root

def reverseLL(head):
    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

arr = list(input().split())
root = arrayToLL(arr)
printLL(root)
root = reverseLL(root)
printLL(root)