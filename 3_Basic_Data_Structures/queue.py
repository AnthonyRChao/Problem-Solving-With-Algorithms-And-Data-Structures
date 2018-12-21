"""
What is a queue?

A queue is a data structure that follows First-In-First-Out order.

Values are added to the rear of the queue and removed from the front.

The simplest example of a queue is a line, or as referred to in many
other parts of the world, queuing!

There is no jumping in the middle or leaving the line early until you
have waited your turn.

Queues are everywhere, from the printer in a school laboratory, to
the operating system of your computer with processes, to real life
grocery store and carnvial lines.
"""

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Adds item to the front of the queue."""
        return self.items.insert(0, item)

    def dequeue(self):
        """Removes item from the back of the queue."""
        return self.items.pop()

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return self.items == []

    def size(self):
        """Returns size as an integer of the queue."""
        return len(self.items)


def main():
    q = Queue()
    print(q.is_empty())
    print(q.enqueue(4))
    print(q.enqueue('dog'))
    print(q.enqueue(True))
    print(q.size())
    print(q.is_empty())
    print(q.enqueue(8.4))
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())


if __name__ == '__main__':
    main()
