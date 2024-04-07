class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.cqueue = [None] * size
        self.front = -1
        self.rear = -1


    def enqueue(self, value: any) -> None:
        if self.front == -1 and self.rear == -1:
            self.rear = self.front = 0
        elif self.rear == self.size-1:
            print("Queue Full")
            return
        else:
            self.rear += 1
        self.cqueue[self.rear] = value


    def dequeue(self) -> None:
        if self.front == -1 and self.rear == -1:
            print("Empty Queue")
            return
        else:
            self.cqueue[self.front] = None
            self.front += 1


    def printCqueue(self) -> None:
        print(self.cqueue)





cqueue = CircularQueue(5)

print("Print cqueue: ")
cqueue.printCqueue()
print("Dequeue: ")
cqueue.dequeue()
print("Enqueue: ")
cqueue.enqueue(8)
cqueue.enqueue(9)
cqueue.enqueue("Alok")
cqueue.enqueue("Python")
cqueue.printCqueue()
print("Enqueue: ")
cqueue.enqueue(6)
cqueue.printCqueue()
print("Dequeue: ")
cqueue.dequeue()
cqueue.printCqueue()
print("Enqueue: ")
cqueue.enqueue(8)
cqueue.printCqueue()
print("Dequeue: ")
cqueue.dequeue()
cqueue.printCqueue()