class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value: any) -> None:
        self.queue.append(value)

    def dequeue(self) -> None:
        if len(self.queue) > 0:
            self.queue.pop(0)
        else:
            print("Empty queue")

    def printqueue(self) -> None:
        print(self.queue)


queue = Queue()

print("Enqueue: ")
queue.enqueue(4)
queue.enqueue("Python")
queue.enqueue("Alok")
queue.enqueue("Uvicorn")
queue.printqueue()
queue.enqueue(6)
queue.printqueue()
print("Dequeue: ")
queue.dequeue()
queue.printqueue()