class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    my_stack = Stack()
    
    print(my_stack.is_empty())
    
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    
    print(my_stack.peek())
    print(my_stack.size())
    
    print(my_stack.pop())
    print(my_stack.peek())