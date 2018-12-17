"""
Write a boolean function that will take two strings and return whether
they are anagrams

anagram('python', 'typhon') => True
anagram('hello', 'goodbye') => False
"""


def anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    for char in word1:
        if char not in word2:
            return False

    return True

def main():
    print(anagram('python', 'typhon'))
    print(anagram('heart', 'earth'))
    print(anagram('hello', 'goodbye'))


if __name__ == '__main__':
    print("I am running by myself")
    main()
else:
    print("I am being imported from another module")
