class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        """linkedlist barcha elementlarini chiqarish"""

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print(">----|----<")

    def push(self, new_data):
        """linkedlist boshiga element qoshish"""

        newnode = Node(new_data)
        newnode.next = self.head
        self.head = newnode

    def insertafter(self, prevnode, newdata):
        """linkedlist o'rta qismlariga element qoshish"""

        if prevnode is None:
            print("tugun mavjud emas")
            return
        newnode = Node(newdata)
        newnode.next = prevnode.next
        prevnode.next = newnode

    def append(self, newdata):
        """linkedlist oxiriga element qoshish"""

        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    def deletenode(self, target):
        """linkedlistdan elementni ochirish"""

        temp = self.head

        if (temp and temp.data == target):
            self.head = temp.next
            temp = None
            return

        while temp:
            if temp.data == target:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None


"""linkedlistga elementlar berish"""
ll = Linkedlist()
ll.head = Node("february")
uch = Node("march")
tort = Node("aprel")
besh = Node("may")
olti = Node("may oxiri")

ll.head.next = uch
uch.next = tort
tort.next = besh
besh.next = olti

ll.printlist()

"""LL ga boshiga element qoshish"""
ll.push("january")
ll.push("December")
ll.push("nov oxiri")
ll.push("November")
ll.push("okt oxiri")
ll.printlist()

"""LL ichiga element qoshish"""
ll.insertafter(olti, "june")
ll.insertafter(olti.next, "june oxiri")
ll.insertafter(olti.next.next, "july")
ll.insertafter(olti.next.next.next, "august")
ll.insertafter(olti.next.next.next.next, "september")
ll.printlist()

"""LL ga oxiridan element qoshish"""
ll.append("october")
ll.append("november")
ll.append("dec boshi")
ll.append("december")
ll.append("dec oxiri")
ll.printlist()

"""LL dan element ochirish"""
ll.deletenode("December")
ll.deletenode("may oxiri")
ll.deletenode("okt oxiri")
ll.deletenode("November")
ll.deletenode("nov oxiri")
ll.deletenode("okt oxiri")
ll.deletenode("dec boshi")
ll.deletenode("dec oxiri")
ll.deletenode("june oxiri")
ll.printlist()



