"""
Write a function that takes a string as a parameter and returns True if the
string is a palindrome, False otherwise.
"""


from string import ascii_lowercase


def palindrome(mystr):

    mystr = mystr.lower()

    mystr_char_list = []
    for char in mystr:
        if char in ascii_lowercase:
            mystr_char_list.append(char)
    mystr_chars = ''.join(mystr_char_list)

    if len(mystr_chars) == 0 or len(mystr_chars) == 1:
        return True
    else:
        if mystr_chars[0] == mystr_chars[-1]:
            return palindrome(mystr_chars[1:len(mystr_chars) - 1])
        else:
            return False


def main():
    print(palindrome("racecar"))
    print(palindrome("kayak"))
    print(palindrome("Live not on evil"))
    print(palindrome("aibohphobia"))
    print(palindrome("Reviled did I live, said I, as evil I did deliver"))
    print(palindrome("Go hang a salami; I'm a lasagna hog."))
    print(palindrome("Able was I ere I saw Elba"))
    print(palindrome("Kanakanak"))
    print(palindrome("Wassamassaw"))


if __name__ == "__main__":
    main()
