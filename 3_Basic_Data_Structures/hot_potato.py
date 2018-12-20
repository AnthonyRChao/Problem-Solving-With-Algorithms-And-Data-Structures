"""
Hot Potato Simulation
"""

from queue import Queue


def hotPotato(l, num):

    q = Queue()

    # Load the queue
    for person in l:
        q.enqueue(person)

    # Cycle num times while q.size() is greater than 1
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()


def main():
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 2))


if __name__ == "__main__":
    main()

