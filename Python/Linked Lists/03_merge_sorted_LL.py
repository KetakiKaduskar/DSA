class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert(root, val):
    temp = Node(val)
    temp.next = root
    root = temp
    return root

def arrToLL(arr):
    root = None
    for i in range(len(arr) - 1, -1, -1):
        root = insert(root, arr[i])

    return root

def mergeSortedLL(head1, head2): 
    one = head1
    two = head2
    res = []

    while one is not None and two is not None:
        if one.data < two.data: 
            res.append(one.data) 
            one = one.next
        else:
            res.append(two.data) 
            two = two.next

    while one is not None:
        res.append(one.data) 
        one = one.next

    while two is not None:
        res.append(two.data) 
        two = two.next

    return res

def displayLL(head): 
    while head is not None: 
        print(head.data, end="->") 
        head = head.next 
    print("")

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

head1 = arrToLL(arr1)
head2 = arrToLL(arr2)

res = mergeSortedLL(head1, head2)
resHead = arrToLL(res)

displayLL(head1)
displayLL(head2)
displayLL(resHead)