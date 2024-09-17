class Node:
    def _init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):

    if head is None or head.next is None:
        return False

    slow = head
    fast = head

    while(fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node (4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head

print(detectCycle(head))