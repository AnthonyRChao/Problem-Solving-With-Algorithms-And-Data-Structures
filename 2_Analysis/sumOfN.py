import time


def sumOfN2(n):

    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum = theSum + i

    end = time.time()

    print(theSum, end - start)
    return theSum, end - start


def sumOfN3(n):
    start = time.time()
    theSum = (n * (n+1)) / 2
    end = time.time()
    return theSum, end - start


if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
