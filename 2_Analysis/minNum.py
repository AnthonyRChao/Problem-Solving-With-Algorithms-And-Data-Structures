"""
Write two Python functions to find the minimum number in a list.

The first function should compare each number to every other number
on the list.  O(n^2).  The second function should be linear O(n).
"""

from time import time
from random import randint


def minNum1(nums):
    start = time()
    minNum = nums[0]
    for num in nums:
        for num in nums:
            if num < minNum:
                minNum = num
    end = time()
    return minNum, end - start


def minNum2(nums):
    start = time()
    minNum = nums[0]
    for num in nums:
        if num < minNum:
            minNum = num
    end = time()
    return minNum, end - start


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
    nums = []
    for i in range(10000):
        nums.append(randint(1, 100))

    print(minNum2(nums))
    print(minNum1(nums))
