# Dynamic Array 
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = value
        self.size += 1

    def display(self):
        print("Array elements:")
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()

    def get(self, index):
        if index < 0 or index >= self.size:
            print("Invalid index")
        else:
            print("Element:", self.array[index])

    def remove(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]

                self.array[self.size - 1] = None
                self.size -= 1
                return

        print("Element not found")


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

arr.display()

arr.get(2)

arr.remove(20)

arr.display()

print("Size:", arr.size)
print("Capacity:", arr.capacity)