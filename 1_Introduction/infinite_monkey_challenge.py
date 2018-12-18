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
from string import ascii_lowercase

ALLOWED_CHARS = ascii_lowercase + ' '

def generate(n):
    return ''.join(choice(ALLOWED_CHARS) for _ in range(n))

def score(string, goal):
    """
    Compare randomly generated string to the goal, check how many
    letters are correct and return
    """
    check_counter = 0
    string = generate(values)

    for i in range(len(string)):
        if string[i] == goal[i]:
            check_counter += 1

    return check_counter

def run(values, goal):
    """
    Repeatedly call generate and score, if letters are correct
    return
    """
    string= ''
    cache = {}
    run_counter = 0

    while not score(string, goal) == len(goal):
        string = generate(values)
        run_counter += 1
        if run_counter % 1000 == 0:
            print(run_counter)
    print('Matching string,', string, 'found at iteration', run_counter)

def main():
    values = ascii_lowercase + ' '
    goal = 'methinks it is like a weasel'
    run(values, goal)


if __name__ == '__main__':
    main()
