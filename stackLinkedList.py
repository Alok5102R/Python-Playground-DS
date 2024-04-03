class Stack:
    def __init__(self, value: any, next: object = None) -> None:
        self.value = value
        self.next = next


newHead = None

def push(head: Stack, value: any) -> Stack:
    if head:
        prevHead = head
        newElement = Stack(value)
        while head.next != None:
            head = head.next
        head.next = newElement
        return prevHead
    else:
        head = Stack(value)
        return head

def pop(head: Stack) -> Stack:
    if head:
        if head.next == None:
            head = None
        else:
            temp2 = head
            while temp2.next != None:
                temp1 = temp2
                temp2 = temp2.next
            temp1.next = None
    return head

def peek(head: Stack) -> any:
    if head:
        while head.next != None:
            head = head.next
        return head.value
    else:
        return None

def printElements(head: Stack) -> None:
    while head:
        print(head.value)
        head = head.next


print("push running: ")
currentHead = push(newHead, 5)
currentHead = push(currentHead, 7)
currentHead = push(currentHead, 9)
print("Stack elements: ")
printElements(currentHead)

print("pop running x2: ")
currentHead = pop(currentHead)
currentHead = pop(currentHead)
print("peak called: ")
print(peek(currentHead))
print("pop running x1: ")
currentHead = pop(currentHead)

print("peak called: ")
print(peek(currentHead))
