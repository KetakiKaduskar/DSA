class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data) 
        if not self.head: 
            self.head = newNode
        else:
            node = self.head 
            while node.next: 
                node = node.next 
            node.next = newNode

    def display(self):
        node = self.head
        while node:
            print(node.data, end="->")
            node = node.next
        print("")

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

def intersectPoint(ll1, ll2): 
    n1 = ll1.head 
    n2 = ll2.head

    delta = abs(ll1.size() - ll2.size())

    if ll1.size() > ll2.size(): 
        for _ in range(delta): 
            n1 = n1.next
    else:
        for _ in range(delta): 
            n2 = n2.next

    while n1 and n2: 
        if n1 == n2: 
            return n1.data 
        n1 = n1.next 
        n2 = n2.next

    return None

def attachAtNode(l1, l2, nodeVal):
    curr1 = l1.head 
    curr2 = l2.head

    while curr1:
        if curr1.data == nodeVal: 
            break 
        curr1 = curr1.next

    if curr1: 
        while curr2.next: 
            curr2 = curr2.next 
        curr2.next = curr1 
        curr1 = curr1.next

list1 = LinkedList()
list1.add(1) 
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
list1.add(6)
list1.add(7)
list1.add(8)

list2 = LinkedList()
list2.add(9)
list2.add(10)
list2.display()
attachAtNode(list1, list2, 5)
list2.display()

print(intersectPoint(list1, list2))