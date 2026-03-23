class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        removed = self.top
        self.top = self.top.next
        return removed.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()     
print(s.pop())  
s.display()     