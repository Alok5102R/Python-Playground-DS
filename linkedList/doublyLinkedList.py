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

    def displayListReverse(self) -> None:
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

    def insertFirst(self, value: any) -> None:
        if self.head:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            newNode = Node(value)
            self.head = newNode

    def insertEnd(self, value: any) -> None:
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

    def deleteEnd(self) -> None:
        if self.head:
            temp = self.head
            while self.head.next != None:
                temp1 = self.head
                self.head = self.head.next
            temp1.next = None
            self.head = temp
        else:
            pass

    def deleteFirst(self) -> None:
        if self.head:
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            print("Empty List")

    def insertBetween(self, index: int, value: any) -> None:
        if self.head:
            temp = self.head
            for _ in range(index-1):
                if self.head:
                    self.head = self.head.next
                else:
                    print("Index out of range")
                    return
            newElement = Node(value, self.head, self.head.next)
            self.head.next = newElement
            self.head = temp
        else:
            print("Empty List")

    def deleteBetween(self, index: int) -> None:
        if self.head:
            temp1 = self.head
            for _ in range(index-1):
                if self.head:
                    self.head = self.head.next
                else:
                    print("Index out of range")
                    return
            temp = self.head.next
            if temp != None:
                self.head.next = temp.next
            else:
                self.head = temp1
                print("Reached to the end")
                return
            temp.prev = self.head
            self.head = temp1
        else:
            print("Empty List")





link = DoublyLinkedList()
link.insertFirst(5)
link.insertFirst(8)
link.insertFirst(19)
link.insertFirst('Alok')
link.insertFirst('Python')
link.insertFirst('Uvicorn')
link.insertEnd(9)
print("Print List: ")
link.displayList()
print("Print List Reversed: ")
link.displayListReverse()
print("Delete end: ")
link.deleteEnd()
link.displayList()
print("Delete first: ")
link.deleteFirst()
link.displayList()
print("Insert between: ")
link.insertBetween(1,'ASGI')
link.displayList()
print("Delete between: ")
link.deleteBetween(3)
link.displayList()

