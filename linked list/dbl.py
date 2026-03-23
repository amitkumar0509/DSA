class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def display_reverse(self):
        if self.head is None:
            return

        
        temp = self.head
        while temp.next:
            temp = temp.next

        
        while temp:
            prev_data = temp.prev.data if temp.prev else "null"
            next_data = temp.next.data if temp.next else "null"

            print(f"[{prev_data} | {temp.data} | {next_data}]", end="")

            if temp.prev:
                print(" <-> ", end="")

            temp = temp.prev
        print()
    def print_dll(self):
        temp = self.head
        while temp:
            prev_val = temp.prev.data if temp.prev else "null"
            next_val = temp.next.data if temp.next else "null"
            print(f"[{prev_val} | {temp.data} | {next_val}]",end="")
            if temp.next:
                print(" <-> ", end="")
            temp = temp.next
        print()
        
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("Doubly Linked List:")
    dll.print_dll()
    print("Reverse Doubly Linked List:")
    dll.display_reverse()