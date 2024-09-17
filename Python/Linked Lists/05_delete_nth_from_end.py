class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            node = self.head 
            while node.next is not None: 
                node = node.next 
            node.next = newNode

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
        print("")

    def delNthFromEnd(self, N):
        slow = self.head
        fast = self.head

        for _ in range(N):
            fast = fast.next

        prev = None

        while fast:
            prev = slow
            fast = fast.next
            slow = slow.next

        if not prev:
            return self.head.next
        else:
            prev.next = slow.next

        return self.head

ll = LinkedList()
ll.add("ha")
ll.add(2)
ll.add("!")
ll.add("    ")
ll.add(-576)
ll.add(1001)
ll.display()
ll.delNthFromEnd(3)
ll.display()