"""
Write a recursive implementation of a binary search function.
"""


def binary_search(haystack, needle):
    if len(haystack) == 0:
        print('Needle not found!')
        return False
    else:
        mid_index = len(haystack) // 2
        print('haystack is {}, mid_index is {}, needle is {}'.format(haystack, mid_index, needle))
        if needle == haystack[mid_index]:
            print('Needle found!')
            return True
        elif needle < haystack[mid_index]:
            return binary_search(haystack[:mid_index], needle)
        else:
            return binary_search(haystack[mid_index + 1:], needle)


# binary_search([1, 2, 3, 4, 5], 4)
binary_search([2, 4, 6, 9, 11, 15], 3)
