"""
What does infix mean?
A + B
A + B * C
(A + B) * C

What does prefix mean?
+ A B
+ A * B C
* + A B C

What does postfix mean?
A B +
A B C * +
A B + C *

The position of operator in relation to operands defines the in, pre or post.

Write an algorithm to convert an infix position expression to its
corresponding postfix expression. Assume the infix expression is a
string of tokens delimited by spaces. The operator tokens are *, /, +,
and -, along with the left and right parentheses, ( and ). The operand
tokens are the single-character identifiers A, B, C, and so on.

1. Create a stack to keep track of operators.  Create a list for output
2. Convert input expression to a list via `split`
3. Iterate through input expression list
3a. If value is an operand, append it to the output list
3b. If value is left parentheses, push it on to the stack
3c. If value is a right parentheses, pop the stack until the corresponding
    left parentheses is removed. Append each operator to the end of the output
    list
3d. If value is an operator, push it on to the stack. However, if there are any
    operators with higher or equal precedence on the stack, first pop them and
    append them to the end of the output list.
4. After iterating through the input expression list, check the stack and
   append any remaining operators to the end of the output list.

"""

# Why are we using a stack? (reversal property, but how?)
# What are the logical steps?
# What are you trying to accomplish?
# Go from Infix to Postfix

# A + B => A B +
# A + B * C => A B C * +
# A * B + C * D => A B * C D * +
# ((A * B) + (C * D))
# Operators are "+-*/()"

# iterate through the space delimited expression, when you encounter
# operator, what do you do? add it to the stack
# do we need to parenthesize the expression?

from string import ascii_uppercase
from stack import Stack


def infix_to_postfix(expr):
    """Convert an infix expression to its postfix equivalent."""

    opstack = Stack()
    vals = expr.split()
    digits = [str(x) for x in range(100)]
    result = []
    prec = {"**":4,
            "*": 3,
            "/": 3,
            "+": 2,
            "-": 2,
            "(": 1,
            }

    for val in vals:
        if val in ascii_uppercase or val in digits:
            result.append(val)
        elif val == "(":
            opstack.push(val)
        elif val == ")":
            top = opstack.pop()
            while top != "(":
                result.append(top)
                top = opstack.pop()
        else:
            while not opstack.is_empty() and prec[opstack.peek()] >= prec[val]:
                result.append(opstack.pop())
            opstack.push(val)

    while not opstack.is_empty():
        result.append(opstack.pop())

    return " ".join(result)


def main():
    """Main function."""

    print(infix_to_postfix("( A + B ) * ( C + D )"))
    print(infix_to_postfix("( A + B ) * C"))
    print(infix_to_postfix("A + B * C"))
    print(infix_to_postfix("10 + 3 * 5 / ( 16 - 4 )"))
    print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))


if __name__ == "__main__":
    main()
