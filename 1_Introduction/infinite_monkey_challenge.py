"""
Self Check

Here’s a self check that really covers everything so far. You may have
heard of the infinite monkey theorem? The theorem states that a monkey
hitting keys at random on a typewriter keyboard for an infinite amount
of time will almost surely type a given text, such as the complete works
of William Shakespeare. Well, suppose we replace a monkey with a Python
function. How long do you think it would take for a Python function to
generate just one sentence of Shakespeare? The sentence we’ll shoot for
is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your
favorite Python IDE. The way we’ll simulate this is to write a function
that generates a string that is 28 characters long by choosing random
letters from the 26 letters in the alphabet plus the space. We’ll write
another function that will score each generated string by comparing the
randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100%
of the letters are correct we are done. If the letters are not correct
then we will generate a whole new string.To make it easier to follow
your program’s progress this third function should print out the best
string generated so far and its score every 1000 tries.


Self Check Challenge

See if you can improve upon the program in the self check by keeping
letters that are correct and only modifying one character in the best
string so far. This is a type of algorithm in the class of ‘hill
climbing’ algorithms, that is we only keep the result if it is better
than the previous one.
"""

from random import choice


def generate(values):
    """Generate a 28 character long string by choosing random letters
    from the 26 letter alphabet plus the space.
    """
    string = ''

    for _ in range(len(values)):
        string += choice(values)

    return string

def score(string, goal):
    """Compare randomly generated string to the goal
    """
    return string == goal

def run():
    """
    Repeatedly call generate and score, if letters are correct
    return
    """

    goal = 'methinks it is like a weasel'
    values = 'abcdefghijklmnopqrstuvwxyz '
    run_counter = 0

    #if not score(generate(values), goal):
    #    counter += 1

    pass



