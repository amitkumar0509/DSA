class Stack:
    def __init__(self,cap):
        self.capacity = cap
        self.arr = [0] *self.capacity
        self.top = -1

    def push(self,x):
        if self.top == self.capacity -1:
            print("stack is overflow!!!!")
            return 
        self.top +=1
        self.arr[self.top]=x
    def pop(self):
        if self.top == -1:
            print("stack is overflow!!!")
            return
        val = self.arr[self.top]
        self.top -=1
        return val
    def peek(self):
        if self.top == -1:
            print("Stack is empty ")
            return
        return self.arr[self.top]
    def isEmpty(self):
        return self.top == -1


    def isFull(self):
        return self.top == self.capacity - 1


if __name__ == "__main__":
    st = myStack(4)