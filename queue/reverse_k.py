from collections import deque
def reverse_k_elements(queue, k):
    if k <= 0 or k > len(queue):
        return

    stack = []

    for _ in range(k):
        stack.append(queue.popleft())

    
    while stack:
        queue.appendleft(stack.pop())

   
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())

q = deque([10, 20, 30, 40, 50, 60, 70, 80])
k = 4
print("Original Queue:")
print(list(q))
reverse_k_elements(q, k)
print("Queue after reversing first", k, "elements:")
print(list(q))
