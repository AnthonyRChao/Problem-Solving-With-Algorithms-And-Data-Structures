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

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
                return found
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while current != None and not found:
            if current.data == item:
                found = True
                previous = current.getNext()
            else:
                previous = current
                current = current.getNext()


def main():
    mylist = UnorderedList()
    print(mylist.add(31))
    print(mylist.add(77))
    print(mylist.add(17))
    print(mylist.add(93))
    print(mylist.add(26))
    print(mylist.add(54))
    print(mylist.search(17))


if __name__ == '__main__':
    main()
