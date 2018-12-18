"""
Stack

A stack is a data structure that follows Last-In First-Out (LIFO),
like a stack of cafeteria trays.

Stacks are fundamentally important, as they can be used to reverse
the order of items.

The order of insertion is the reverse of the order of removal.

Another great example of a stack is your browser's Back button.  As you
move from web page to web page, those pages are placed on a stack
(actually it is the URLs that are going on the stack).  The current page
is on the top of the stack and the first page you looked is the base.
If you click on the back button you move in reverse order through the
pages.
"""


class Stack:
    """
    An implementation of the Stack data structure
    """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """
        Check if Stack is empty
        """
        return self.items == []

    def push(self, item):
        """
        Add item to top of Stack
        """
        return self.items.append(item)

    def pop(self):
        """
        Remove item from top of Stack
        """
        return self.items.pop()

    def peek(self):
        """
        Look at item from top of Stack
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Return size of Stack
        """
        return len(self.items)
