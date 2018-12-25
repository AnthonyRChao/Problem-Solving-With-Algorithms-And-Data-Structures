"""An Unordered List Implementation."""


from Node import Node


class UnorderedList:

    def __init__(self):
        self.head = None
        self.next = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
       temp = Node(item)
       temp.setNext(self.head)
       self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
