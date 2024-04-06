class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.cqueue = [None] * size
        self.front = 0
        self.rear = -1

    def enqueue(self, value: any) -> None:
        self.rear += 1
        self.cqueue[self.rear] = value

    def dequeue(self) -> None:
        self.cqueue[self.front] = None
        self.front += 1

    def printCqueue(self) -> None:
        print(self.cqueue)

cqueue = CircularQueue(10)

cqueue.printCqueue()
cqueue.enqueue(5)
cqueue.enqueue(6)
cqueue.printCqueue()
cqueue.dequeue()
cqueue.printCqueue()