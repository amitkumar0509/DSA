class BinarySearchtTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchtTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchtTreeNode(data)
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements  += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
def build_tree(elements):
    root = BinarySearchtTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    
    # countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)
    number_tree = build_tree(numbers)
    number_tree.delete(20)
    print("In order traversal gives sorted order of elements:")
    print(number_tree.in_order_traversal())
    # print("In order traversal gives sorted order of elements:")
    # print(number_tree.in_order_traversal())
    # print(number_tree.search(20))
    # print(country_tree.in_order_traversal())
    # print(country_tree.search("Nigeria"))
    # print("Min:",number_tree.find_min())
    # print("Max:",number_tree.find_max())



    # root = BinarySearchtTreeNode(numbers[0])
    # for number in numbers[1:]:
    #     root.add_child(number)
    # print("In order traversal gives sorted order of elements:")
    # print(root.in_order_traversal())