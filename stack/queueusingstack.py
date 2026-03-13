class myQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def push(self, x):
        self.s1.append(x)
    def pop(self):
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    def peek(self):
        if not self.s2:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    def empty(self):
        return not self.s1 and not self.s2
    
    def display(self):
        # Display all values in queue order (front to back)
        if self.empty():
            print("Queue is empty")
            return
        # s2 has front elements (reversed), s1 has back elements
        queue_values = self.s2[::-1] + self.s1
        print("Queue:", queue_values)
        return queue_values

if __name__ == "__main__":
    q = myQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print("After pushing 1, 2, 3:")
    q.display()
    
    print("\nPeek:", q.peek())
    print("After peek:")
    q.display()
    
    print("\nPopped:", q.pop())
    print("After pop:")
    q.display()
    
    q.push(4)
    q.push(5)
    print("\nAfter pushing 4, 5:")
    q.display()
    
    print("\nIs empty?", q.empty())

