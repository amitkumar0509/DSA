class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity

    # 1. Enqueue operation
    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow! Cannot enqueue.")
            return
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # 2. Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue.")
            return None
        removed = self.queue.pop(0)
        print(f"Dequeued: {removed}")
        return removed

    # 3. Peek / Front operation
    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[0]

    # 4. Rear operation
    def rear(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[-1]

    # 5. isEmpty operation
    def is_empty(self):
        return len(self.queue) == 0

    # 6. isFull operation
    def is_full(self):
        return len(self.queue) == self.capacity

    # 7. Size operation
    def size(self):
        return len(self.queue)

    # 8. Display operation
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:", self.queue)


# ----------- Driver Code (Testing All Operations) -----------

q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front element:", q.front())
print("Rear element:", q.rear())

q.dequeue()
q.display()

print("Queue size:", q.size())
print("Is queue empty?", q.is_empty())
print("Is queue full?", q.is_full())
