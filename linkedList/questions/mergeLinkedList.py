# l1 = [1,2,3] | l2 = [1,4,7] | lmerged = [1,1,2,4,3,7]
# To run this: python -m linkedList.questions.mergeLinkedList

from .. import linkedList


ls1 = linkedList.LinkedList()
ls2 = linkedList.LinkedList()

ls1.insertEnd(1)
ls1.insertEnd(2)
ls1.insertEnd(3)

ls2.insertEnd(1)
ls2.insertEnd(4)
ls2.insertEnd(7)

print("ls1: ")
ls1.printNode()
print("ls2: ")
ls2.printNode()

class MergeList(linkedList.LinkedList):
    def __init__(self):
        super().__init__()

    def mergeLinkedList(self, list1: linkedList.LinkedList, list2: linkedList.LinkedList):
        self.head1 = list1
        self.head2 = list2
        self.newhead = linkedList.LinkedList()

        while self.head1:
            self.newhead.insertEnd(self.head1.value)
            self.head1 = self.head1.next
        self.newhead.printNode()

obj1 = MergeList

obj1.mergeLinkedList(ls1, ls2, ls2)
