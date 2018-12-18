"""
Write a function revstring(mystr) that uses a stack to reverse the characters in a string.
"""

from stack import Stack


def revstring(mystr):

    s = Stack()
    result = ""

    for char in mystr:
        s.push(char)

    while not s.is_empty():
        result += s.pop()

    return result


def main():
    print(revstring('hello'))
    print(revstring('darkness'))
    print(revstring('my old friend'))


if __name__ == "__main__":
    main()
