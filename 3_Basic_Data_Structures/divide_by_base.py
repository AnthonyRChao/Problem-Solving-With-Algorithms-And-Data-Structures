"""
Write an algorithm to convert a decimal number into a given base number.
"""

from stack import Stack


def dec_to_bin(num, base):
    """ Converts a decimal number to a number of specified base.

    Args:
        num: A positive integer.
        base: A positive integer.

    Returns:
        A integer of specified base.

    Raises:
        None
    """

    # Divide number by base and keep track of remainder in a stack.
    # What is one of the key indicators that a stack should be used?
    # Reversability
    # The reversal property signals that a stack is likely the appropriate
    # data structure for solving the problem.

    result = ""
    remstack = Stack()
    digits = "0123456789ABCDEF"

    while num > 0:
        rem = num % base
        num = num // base
        remstack.push(rem)

    while not remstack.is_empty():
        result += digits[remstack.pop()]

    return result


def main():
    """Okay Syntastic"""
    print(dec_to_bin(25, 8))
    print(dec_to_bin(256, 16))
    print(dec_to_bin(26, 26))


if __name__ == "__main__":
    main()
