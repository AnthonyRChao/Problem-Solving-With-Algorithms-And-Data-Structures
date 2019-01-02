"""
Write an iterative implementation of a binary search function.
"""


def binary_search(haystack, needle):
    first = 0
    last = len(haystack) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        print('haystack is {}, mid is {}, first is {}, last is {}'.format(
            haystack, mid, first, last))
        if haystack[mid] == needle:
            found = True
        elif haystack[mid] < needle:
            first = mid + 1
        else:
            last = mid - 1
    return found


print(binary_search([2, 4, 6, 8, 9, 11, 15],  11))
