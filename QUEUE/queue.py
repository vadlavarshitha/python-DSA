class Queue:
    def __init__(self):
        self.items = []   

    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty!")
            return None

    
    def peek(self):
        if not self.is_empty():
            print(f"Front item: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty!")
            return None


    def size(self):
        print(f"Queue size: {len(self.items)}")
        return len(self.items)

    
    def is_empty(self):
        return len(self.items) == 0

    
    def display(self):
        if not self.is_empty():
            print("Queue contents:", self.items)
        else:
            print("Queue is empty!")


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()          
q.peek()
q.size()             

q.dequeue()
q.display()          

q.dequeue()
q.dequeue()
q.dequeue()          
