"""
Write a function that takes a string as a parameter and returns a
new string that is the reverse of the old string.
"""


def reverse_string(mystr):
    if mystr == "":
        return mystr
    else:
        return reverse_string(mystr[1:]) + mystr[0]


def main():
    print(reverse_string("hello"))


if __name__ == "__main__":
    main()
