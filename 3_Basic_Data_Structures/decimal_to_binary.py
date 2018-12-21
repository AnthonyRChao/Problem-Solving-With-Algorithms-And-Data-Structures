"""
Write an algorithm to convert a decimal number into a binary number.
"""

from stack import Stack


def dec_to_bin(num):
    """ Converts a decimal number to a binary number.

    Args:
        num: A positive integer.

    Returns:
        A binary integer.

    Raises:
        None
    """

    # Divide number by two and keep track of remainder in a stack.
    # What is one of the key indicators that a stack should be used?
    # Reversability
    # The reversal property signals that a stack is likely the appropriate
    # data structure for solving the problem.

    result = ""
    remstack = Stack()

    while num > 0:
        rem = num % 2
        num = num // 2
        remstack.push(rem)

    while not remstack.is_empty():
        result += str(remstack.pop())

    return result


def main():
    print(dec_to_bin(233))


if __name__ == "__main__":
    main()
