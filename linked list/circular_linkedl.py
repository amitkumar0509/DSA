class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head        # points to itself
            return
        curr = self.head
        while curr.next != self.head:        # find last node
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head            # new node points back to head

    def prepend(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:        # reach last node
            curr = curr.next
        new_node.next = self.head
        curr.next = new_node                 # last node → new node
        self.head = new_node                 # update head

    def delete(self, val):
        if not self.head:
            return
        # Case 1: deleting head
        if self.head.val == val:
            if self.head.next == self.head:  # only one node
                self.head = None
                return
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next       # last → second node
            self.head = self.head.next
            return
        # Case 2: deleting non-head node
        curr = self.head
        while curr.next != self.head:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def traverse(self):
        if not self.head:
            return []
        result = []
        curr = self.head
        while True:
            result.append(curr.val)
            curr = curr.next
            if curr == self.head:            # back to head → stop
                break
        return result


# ── Demo ─────────────────────────────────────────────
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)

print("After appending 1→4 :", cll.traverse())   # [1, 2, 3, 4]

cll.prepend(0)
print("After prepending  0 :", cll.traverse())   # [0, 1, 2, 3, 4]

cll.delete(2)
print("After deleting    2 :", cll.traverse())   # [0, 1, 3, 4]
