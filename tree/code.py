class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

root = TreeNode("Electronics")

tv = TreeNode("Televisions")
phones = TreeNode("Mobile Phones")
laptops = TreeNode("Laptops")

root.add_child(tv)
root.add_child(phones)
root.add_child(laptops)

smart_tv = TreeNode("Smart TVs")
led_tv = TreeNode("LED TVs")
tv.add_child(smart_tv)
tv.add_child(led_tv)

samsung_tv = TreeNode("Samsung")
lg_tv = TreeNode("LG")
smart_tv.add_child(samsung_tv)
smart_tv.add_child(lg_tv)

android = TreeNode("Android Phones")
iphone = TreeNode("iPhones")
phones.add_child(android)
phones.add_child(iphone)

samsung_phone = TreeNode("Samsung Galaxy")
android.add_child(samsung_phone)

apple_iphone = TreeNode("iPhone 15")
iphone.add_child(apple_iphone)

gaming = TreeNode("Gaming Laptops")
work = TreeNode("Work Laptops")
laptops.add_child(gaming)
laptops.add_child(work)

def display_tree(node, level=0):
    print("  " * level + "|-- " + node.name)
    for child in node.children:
        display_tree(child, level + 1)

print("Electronics Items Tree:\n")
display_tree(root)
