class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
class Avl:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    def get_balance(self,root):
        if not root:
            return 0 
        return self.get_height(root.left)
    def rigtht_rotate(self, y):
        x = y.left
        T2 = y.right
        y.right = x
        x.left = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return x
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and key < root.left.val:
            return self.rigtht_rotate(root)
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.rigtht_rotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rigtht_rotate(root.right)
            return self.left_rotate(root)
        return root
def pre_order(root):
    if not root:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val ,end = " ")
    inorder(root.right)
def post_order(root):
    if not root:
        return 0
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" ")

if __name__ == "__main__":
    avl_tree = Avl()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl_tree.insert(root, key)
    print("Preorder traversal of the AVL tree is:")
    pre_order(root)
    print("\nInorder traversal of the AVL tree is:")
    inorder(root)
    print("\nPostorder traversal of the AVL tree is:")
    post_order(root)