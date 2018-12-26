"""A recursive implementation for the sum of a list of numbers."""


def listsum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + listsum(nums[1:])


def main():
    print(listsum([1, 3, 5, 7, 9]))


if __name__ == '__main__':
    main()
