class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        # listning boshiga element qo'shish
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        # listning ixtiyoriy nuqtasiga element qo'shish
        if prev_node is None:
            print("Error")
        # yangi element qo'shamiz
        new_node = Node(new_data)
        # yangi tugunni keyingi elementga bog'laymiz
        new_node.next = prev_node.next # a2
        # avvalgi tugunni yangi elementga bog'laymiz
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

# a1 = Node(1)
# a2 = Node(5)
# a3 = Node(45)
#
# ll = LinkedList()
# ll.head = a3
# a3.next = a1
# a1.next = a2
# ll.printList()
# # a3 - a1 - a2
# print("_________")
# ll.append(101)
# ll.printList()

data = list(range(1, 100))
a1 = Node(data[0])
ll = LinkedList()
ll.head = a1
for i in data[1:]:
    new_node = Node(i)
    last = ll.head
    while last.next:
        last = last.next
    last.next = new_node
print(type(ll))

