class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def preorder_stack(root):     # Root → Left → Right
    if not root:
        return []
    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result
root = Node(1)
root.left  = Node(2)
root.right = Node(3)
root.left.left  = Node(4)
root.left.right = Node(5)

print(preorder_stack(root))