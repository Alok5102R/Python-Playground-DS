class Node:
    def __init__(self, value: any, prev: object = None, next: object = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def displayList(self) -> None:
        if self.head:
            temp = self.head
            while self.head:
                print(self.head.value)
                self.head = self.head.next
            self.head = temp
        else:
            print("None")

    def displayListBack(self) -> None:
        if self.head:
            temp = self.head
            while self.head.next != None:
                self.head = self.head.next
            while self.head:
                print(self.head.value)
                self.head = self.head.prev
            self.head = temp
        else:
            print("None")

    def insertFirst(self, value) -> object:
        if self.head:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            newNode = Node(value)
            self.head = newNode

    def insertEnd(self, value) -> object:
        if self.head:
            temp = self.head
            while self.head.next != None:
                self.head = self.head.next
            newNode = Node(value)
            self.head.next = newNode
            newNode.prev = self.head
            self.head = temp
        else:
            newNode = Node(value)
            self.head = newNode


link = DoublyLinkedList()
link.insertFirst(5)
link.insertFirst(8)
link.insertEnd(9)
print("Print List: ")
link.displayList()
print("Print List Backward: ")
link.displayListBack()
