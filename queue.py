class Queue:
    def __init__(self):
        self.items = []   # initialize an empty list

    # Enqueue: add item to the end
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    # Dequeue: remove item from the front
    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty!")
            return None

    # Peek: view the front item without removing
    def peek(self):
        if not self.is_empty():
            print(f"Front item: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty!")
            return None

    # Size: number of items in queue
    def size(self):
        print(f"Queue size: {len(self.items)}")
        return len(self.items)

    # Check if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display all items
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

q.display()          # [10, 20, 30]
q.peek()             # Front item: 10
q.size()             # Queue size: 3

q.dequeue()          # Dequeued: 10
q.display()          # [20, 30]

q.dequeue()
q.dequeue()
q.dequeue()          # Queue is empty!
