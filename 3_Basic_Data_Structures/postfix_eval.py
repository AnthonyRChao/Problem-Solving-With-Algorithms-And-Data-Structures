"""Returns the output of a given postfix expression."""
from stack import Stack


def post_eval(expr):
    """Evaluates a postfix expression and returns output."""

    expr = expr.split(" ")
    operand_stack = Stack()
    digits = [str(x) for x in range(100)]

    for val in expr:
        if val in digits:
            operand_stack.push(val)
        else:
            a = operand_stack.pop()
            b = operand_stack.pop()
            operand_stack.push(do_math(a, b, val))

    return operand_stack.pop()


def do_math(a, b, operator):
    """Helper function that performs computation between two numbers."""

    if operator == "+":
        return int(b) + int(a)
    elif operator == "-":
        return int(b) - int(a)
    elif operator == "*":
        return int(b) * int(a)
    elif operator  == "/":
        return int(b) // int(a)


def main():
    """Main function."""
    print(post_eval("4 5 6 * +"))
    print(post_eval("17 10 + 3 * 9 /"))


if __name__ == "__main__":
    main()
