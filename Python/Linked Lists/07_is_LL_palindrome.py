class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

left = Node(None)

def printLL(root): 
    while root is not None: 
        print(root.data, end="->") 
        root = root.next 
    print("")

def insert(root, val): 
    newNode = Node(val) 
    newNode.next = root
    root = newNode 
    return root

def arrToLL(arr):
    root = None 
    for i in range(len(arr) - 1, -1, -1): 
        root = insert(root, arr[i])
    return root

def isLLPalindromeHelper(right, floor):
    global left

    if not right: 
        return True

    recRes = isLLPalindromeHelper(right.next, floor+1)

    if not recRes: 
        return False
    elif right.data != left.data: 
        return False
    else:
        left = left.next
        return True

def sizeLL(head):
    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    return count

def isLLPalindrome(head):
    global left
    left = head
    return isLLPalindromeHelper(head, 0)

arr = list(input().split())
head = arrToLL(arr)
printLL(head)
size = sizeLL(head)

print(isLLPalindrome(head))