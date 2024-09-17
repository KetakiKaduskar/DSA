class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(lot): 
    root = Node(lot[0]) 
    q = [root] 
    idx = 1

    while q and idx < len(lot): 
        node = q.pop(0)

        if idx < len(lot) and lot[idx] != 'n': 
            node.left = Node(lot [idx]) 
            q.append(node.left)
        idx += 1

        if idx < len(lot) and lot [idx] != 'n': 
            node.right = Node(lot[idx]) 
            q.append(node.right)
        idx += 1

    return root

def maxHeight(root):
    if root is None:
        return -1
    maxh = 1 + max(maxHeight(root.left), maxHeight(root.right))
    return maxh

levelOrderTraversal = list(input().split())
root = constructTree(levelOrderTraversal)
print(maxHeight(root))