
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

# Example usage:

queue = Queue()

queue.enqueue(4)
queue.enqueue(6)
queue.enqueue(2)
queue.enqueue(7)
queue.enqueue(10)

for i in range(queue.size()):
    print(queue.items)
    x = queue.dequeue()
    print("x:", x)



