"""
Write an algorithm that checks if a symbol string is balanced.

For example

{{[][]}()} => True
{{[[(())]] => False
"""

from stack import Stack

OPENERS = "{[("
CLOSERS = "}])"


def symbol_check(mystr):
    # A symbol string is balanced if every opening symbol has a
    # matching closing symbol.  This algorithm uses a stack to
    # store each opening symbol, pushing it onto the stack. 
    # when a closing symbol appears, check if the top (pop)
    # of the stack has a matching opening symbol, if it does,
    # pop the top off and continue moving forwrad, if not
    # the string is not balanced.

    s = Stack()

    for char in mystr:
        if char in OPENERS:
            s.push(char)
        else:
            top = s.pop()
            print(CLOSERS)
            print(CLOSERS.index(top))
            if OPENERS.index(char) == CLOSERS.index(top):
                return False
    return s.is_empty()

def match(open, close):
    pass

def main():
    print(symbol_check("{}"))
    print(symbol_check("[]"))
    print(symbol_check("()"))
    print(symbol_check("{{[][]}()}"))
    print(symbol_check("{{[[(())]]"))


if __name__ == "__main__":
    main()
