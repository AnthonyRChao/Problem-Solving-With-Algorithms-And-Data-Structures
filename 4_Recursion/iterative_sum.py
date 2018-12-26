"""An iterative implementation for the sum of a list of numbers."""


def listsum1(nums):
    accum = 0
    for num in nums:
        accum += num
    return accum


def listsum2(nums):
    accum = 0
    i = 0
    while i < len(nums):
        accum += nums[i]
        i += 1
    return accum


def main():
    print(listsum1([1, 3, 5, 7, 9]))
    print(listsum2([1, 3, 5, 7, 9]))


if __name__ == '__main__':
    main()
