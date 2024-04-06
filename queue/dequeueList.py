class Dequeue:
    def __init__(self):
        self.dequeue = []

    def frontEnqueue(self, value: any) -> None:
        self.dequeue.insert(0, value)

    def rearEnqueue(self, value: any) -> None:
        self.dequeue.append(value)

    def frontDequeue(self) -> None:
        self.dequeue.pop(0)

    def rearDequeue(self) -> None:
        self.dequeue.pop()

    def printDequeue(self) -> None:
        print(self.dequeue)

dequeue = Dequeue()

print("Front Enqueue: ")
dequeue.frontEnqueue(4)
dequeue.printDequeue()
print("Front Enqueue: ")
dequeue.frontEnqueue(3)
dequeue.printDequeue()
print("Rear Enqueue: ")
dequeue.rearEnqueue("Alok")
dequeue.printDequeue()
print("Front Dequeue: ")
dequeue.frontDequeue()
dequeue.printDequeue()
print("Rear Dequeue: ")
dequeue.rearDequeue()
dequeue.printDequeue()
