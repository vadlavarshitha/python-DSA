class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListAllOperations:
    def __init__(self):
        self.head = None

    

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position!")
            return
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                print("Position out of bounds!")
                return
            temp = temp.next
        
        if temp is None:
            print("Position out of bounds!")
            return
        
        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {data} at position {position}.")

    

    def delete_by_value(self, key):
        if self.head is None:
            print("List is empty!")
            return
        
        if self.head.data == key:
            self.head = self.head.next
            print(f"Deleted node with value {key}.")
            return
        
        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        if temp is None:
            print(f"Value {key} not found in the list.")
            return
        
        prev.next = temp.next
        print(f"Deleted node with value {key}.")

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty!")
            return
        
        if position == 0:
            self.head = self.head.next
            print("Deleted node at position 0.")
            return
        
        temp = self.head
        prev = None
        for _ in range(position):
            if temp is None:
                print("Position out of bounds!")
                return
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("Position out of bounds!")
            return
        
        prev.next = temp.next
        print(f"Deleted node at position {position}.")

    

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        elements = []
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) + " -> None")

    def search(self, key):
        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Value {key} found at position {position}.")
                return True
            temp = temp.next
            position += 1
        print(f"Value {key} not found.")
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked list reversed.")

if __name__ == "__main__":
    linked_list = LinkedListAllOperations()

    
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(30)
    linked_list.insert_at_position(15, 2)
    linked_list.display()

    
    linked_list.search(15)
    linked_list.search(100)

    
    linked_list.delete_by_value(15)
    linked_list.display()

    linked_list.delete_at_position(0)
    linked_list.display()

    
    linked_list.reverse()
    linked_list.display()