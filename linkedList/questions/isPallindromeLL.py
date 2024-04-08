from .. import linkedList

# To run this: python -m linkedList.questions.isPallindromeLL

class Pallindrome(linkedList.LinkedList):
    def __init__(self):
        super().__init__()

    def lengthOfList(self):
        temp = self.head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        print("Length of List: " + str(count))
        return count
    
    def pallindrome(self):
        currentHead = self.head
        temp = self.head
        temp1 = temp
        length = self.lengthOfList()//2
        for _ in range(length):
            print(temp.value)
            temp = temp.next
        print(temp.value)
        self.head = temp
        self.reverseList()
        self.printNode()

        tempHead = self.head
        print("Pallindrome check: ")
        flag = 0
        for _ in range(length):
            if temp1.value == self.head.value:
                flag = 1
            else:
                flag = 0
            temp1 = temp1.next
            self.head = self.head.next
        if flag == 1:
            print("Yes Pallindrome")
        else:
            print("Not Pallindrome")
        self.head = tempHead
        self.reverseList()
        self.head = currentHead


myList = Pallindrome()

myList.insertEnd(1)
myList.insertEnd(2)
myList.insertEnd("Alok")
myList.insertEnd("Alok")
myList.insertEnd(2)
myList.insertEnd(1)
myList.printNode()
myList.lengthOfList()
myList.pallindrome()
myList.printNode()