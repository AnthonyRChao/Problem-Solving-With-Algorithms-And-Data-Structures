"""
Write an algorithm that checks if a symbol string is balanced.

For example

{{[][]}()} => True
{{[[(())]] => False
"""


openers = "{[("
closers = "}])"

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []


def symbol_check(mystr):
    pass

#    s = Stack()
#
#    for char in mystr:
#        if char in openers:
#            s.push(char)
#        elif:
#            s.pop().index() == 

def main():
    print(symbol_check("{{[][]}()}"))
    print(symbol_check("{{[[(())]]"))


if __name__ == "__main__":
    main()
