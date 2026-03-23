class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(node):      # Left → Root → Right
    if node:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def preorder(node):     # Root → Left → Right
    if node:
        print(node.val)
        preorder(node.left)
        preorder(node.right)

def postorder(node):    # Left → Right → Root
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val)

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

print("Inorder Traversal:")
inorder(root)               
# Output: 4 2 5 1 3

print("Preorder Traversal:")
preorder(root)              
# Output: 1 2 4 5 3

print("Postorder Traversal:")
postorder(root)             