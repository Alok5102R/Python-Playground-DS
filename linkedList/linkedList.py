# Node initialization
class Node:
    def __init__(self, value: any, next: object = None):
        self.value = value
        self.next = next



class LinkedList:

    def __init__(self):
        self.head = None

    # Multiple Nodes Creation and Insertion at end
    def createNode(self, numberOfElements: int):
        temp = self.head
        for i in range(numberOfElements):
            value: any = input(f"Enter data{i+1}: ")
            newNode = Node(value)
            temp.next = newNode
            temp = temp.next
    
    # Node iteration
    def printNode(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    # Node Insertion at end
    def insertEnd(self, value: any):
        if self.head:
            temp = self.head
            while self.head.next != None:
                self.head = self.head.next
            newNode = Node(value)
            self.head.next = newNode
            self.head = temp
        else:
            self.head = Node(value)
    
    # Node Insertion at beginning
    def insertFirst(self, value: any):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode


    # Node Insertion in between
    def insertBetween(self, index: int, value: any):
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        newNode = Node(value)
        newNode.next = temp.next
        temp.next = newNode


    # Node Deletion at end
    def deleteEnd(self):
        temp = self.head
        while temp.next != None:
            temp1 = temp
            temp = temp.next
        temp1.next = None


    # Node Deletion at beginning
    def deleteFirst(self):
        temp = self.head.next
        self.head = temp


    # Node Deletion in between
    def deleteBetween(self, index: int):
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        newTemp = temp.next
        temp.next = newTemp.next


    # Node Updation at any index
    def nodeUpdate(self, index: int, value: any):
        temp = self.head
        if(index==0):
            self.head.value = value
        else:
            for _ in range(index):
                self.head = self.head.next
            self.head.value = value
        self.head = temp


    # Reverse Link List
    def reverseList(self):
        prev = None
        current = self.head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev



if __name__ == "__main__":
    myList = LinkedList()

    print("Insert End: ")
    myList.insertEnd(6)
    myList.insertEnd("Alok")
    myList.insertEnd("Python")
    myList.insertEnd(9)
    myList.printNode()
    print("Insert First: ")
    myList.insertFirst("Uvicorn")
    myList.printNode()
    print("Insert Between: ")
    myList.insertBetween(3, "Kumar")
    myList.printNode()
    print("Delete First: ")
    myList.deleteFirst()
    myList.printNode()
    print("Delete End: ")
    myList.deleteEnd()
    myList.printNode()
    print("Delete Between: ")
    myList.deleteBetween(2)
    myList.printNode()
    print("Reverse List: ")
    myList.reverseList()
    myList.printNode()

