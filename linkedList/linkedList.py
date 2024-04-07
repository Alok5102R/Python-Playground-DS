# Node initialization
class Node:
    def __init__(self, value: any, next: object = None):
        self.value = value
        self.next = next


"""
# Can be done Like this:
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # methods .....
"""


# Single Node Creation and Insertion at end
node1 = Node(45)
node2 = Node(89)
node1.next = node2
node3 = Node(109)
node2.next = node3


# Multiple Nodes Creation and Insertion at end
def createNode(numberOfElements: int):
    head = Node(None)
    temp = head
    for i in range(numberOfElements):
        value: any = input(f"Enter data{i+1}: ")
        newNode = Node(value)
        temp.next = newNode
        temp = temp.next
    return head.next


# Node iteration
def printNode(head: Node):
    node = head
    while node:
        print(node.value)
        node = node.next


# Node Insertion at end
def insertEnd(head: Node, value: any):
    temp = head
    while head.next != None:
        head = head.next
    newNode = Node(value)
    head.next = newNode
    return temp


# Node Insertion at beginning
def insertFirst(head: Node, value: any):
    newnode = Node(value)
    newnode.next = head
    return newnode


# Node Insertion in between
def insertBetween(head: Node, index: int, value: any):
    temp = head
    for _ in range(index-1):
        temp = temp.next
    newNode = Node(value)
    newNode.next = temp.next
    temp.next = newNode
    return head


# Node Deletion at end
def deleteEnd(head: Node):
    temp = head
    while temp.next != None:
        temp1 = temp
        temp = temp.next
    temp1.next = None
    return head


# Node Deletion at beginning
def deleteFirst(head: Node):
    temp = head.next
    head = temp
    return head


# Node Deletion in between
def deleteBetween(head: Node, index: int):
    temp = head
    for _ in range(index-1):
        temp = temp.next
    newTemp = temp.next
    temp.next = newTemp.next
    return head


# Node Updation at any index
def nodeUpdate(head: Node, index: int, value: any):
    temp = head
    if(index==0):
        head.value = value
    else:
        for _ in range(index):
            head = head.next
        head.value = value
    return temp


# Reverse Link List
def reverseList(head: Node):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev



# Method calls
print("Insert one: ")
printNode(node1)
print("Insert first: ")
printNode(insertFirst(node1, 68))
print("Insert many: ")
currentListHead = createNode(5)
printNode(currentListHead)
print("Insert between: ")
newListHead = insertBetween(currentListHead, 1, 67)
printNode(newListHead)
print("Insert end: ")
newListHead = insertEnd(currentListHead, 19)
printNode(newListHead)
print("Delete end: ")
newListHead = deleteEnd(newListHead)
printNode(newListHead)
print("Delete first: ")
newListHead = deleteFirst(newListHead)
printNode(newListHead)
print("Delete between: ")
newListHead = deleteBetween(newListHead, 1)
printNode(newListHead)
print("Update any: ")
newListHead = nodeUpdate(newListHead, 2, 378)
printNode(newListHead)
print("Reverse List: ")
printNode(reverseList(newListHead))


