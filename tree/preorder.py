class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def preorder(node):     # Root → Left → Right
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)
def push(node,val):
    if not node:
        return Node(val)
    if val < node.val:
        node.left = push(node.left, val)
    else:
        node.right = push(node.right, val)
    return node



# Constructing the binary tree:
#         1 
#        / \
#       2   3
#      / \
#     4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder Traversal:")
# preorder(root)
if __name__ == "__main__":
    root = None
    values = [1, 2, 3, 4, 5]
    for val in values:
        root = push(root, val)
    print("Preorder Traversal:")
    preorder(root)

