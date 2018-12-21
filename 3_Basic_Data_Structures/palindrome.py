"""Implementation of palindrom checker."""

from deque import Deque


def check(expr):

    chars = Deque()

    for char in expr:
        chars.addRear(char)

    while chars.size() > 1:
        char_one = chars.removeFront()
        char_two = chars.removeRear()
        if char_one != char_two:
            return False

    return True


def main():
    print(check("radar"))
    print(check("toot"))
    print(check("racecar"))
    print(check("moon"))


if __name__ == "__main__":
    main()
