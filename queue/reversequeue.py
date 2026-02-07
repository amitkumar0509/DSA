class Queue:
    def __init__(self):
        self.items = []

  
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


    def display(self):
        print(self.items)


def reverse_queue(queue):
    stack = []


    while not queue.is_empty():
        stack.append(queue.dequeue())

    
    while stack:
        queue.enqueue(stack.pop())


# -------- Driver Code --------
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("Original Queue:")
q.display()

reverse_queue(q)

print("Reversed Queue:")
q.display()
