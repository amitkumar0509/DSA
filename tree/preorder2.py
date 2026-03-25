class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder_without_push(root):
    curr = root

    while curr:
        if curr.left is None:
            print(curr.data, end=" ")
            curr = curr.right
        else:
            # Find inorder predecessor of curr
            pred = curr.left
            while pred.right and pred.right is not curr:
                pred = pred.right

            if pred.right is None:
                # Visit before going left (preorder)
                print(curr.data, end=" ")
                pred.right = curr
                curr = curr.left
            else:
                # Remove thread and go right
                pred.right = None
                curr = curr.right

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder_without_push(root)   # Output: 1 2 4 5 3
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# def preorder(root):
#     if root is None:
#         return
#     print(root.data, end=" ")
#     preorder(root.left)
#     preorder(root.right)


# # Example
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# preorder(root)  # 1 2 4 5 3