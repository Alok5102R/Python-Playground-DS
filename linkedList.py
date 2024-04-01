# Node initialization
class Node:
    def __init__(self, value: any, next: hex = None):
        self.value = value
        self.next = next


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


# Method calls
printNode(insertFirst(node1, 68))
currentListHead = createNode(5)
newListHead = insertBetween(currentListHead, 1, 67)
printNode(newListHead)

