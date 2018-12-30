"""
Write recursive algorithm that rolves the Tower of Hanoi problem.

Explanation:
  The key to the simplicity of this algorithm is that we make two
  different recursive calls. The first recursive call moves all but
  the bottom disk on the initial tower to an intermediate pole. The
  next line simply moves the bottom disk to its final resting place.
  Then the second recursive call moves the tower from the
  intermediate pole on top of the largest disk. The base case is
  detected when the tower height is 0, there is no task to be
  completed so move_tower simply returns.
"""


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)


def main():
    move_tower(4, "A", "C", "B")


if __name__ == "__main__":
    main()
