"""
Write an algorithm that checks whether a string of parentheses is balanced.

check_par("(())") => True
check_par("((()") => False

Start with an empty stack, process the parentheses strings from left to right.
If a symbol is an opening parentheses, push it on to the stack.
If a symbol is a closing parentheses, pop it off the stack.
As long as you are able to pop something off the stack, the string of
parenthesis is balanced.
At the end of the string, the stack should be empty, if it is,
the string is balanced.
"""

from stack import Stack


def check_par(mystr):
    """
    Check if a given string of parentheses is balanced.
    """
    s = Stack()

    for char in mystr:
        if char == "(":
            s.push(char)
        else:
            s.pop()

    return s.is_empty()


def main():
    print(check_par("(())"))
    print(check_par("((()"))


if __name__ == "__main__":
    main()

