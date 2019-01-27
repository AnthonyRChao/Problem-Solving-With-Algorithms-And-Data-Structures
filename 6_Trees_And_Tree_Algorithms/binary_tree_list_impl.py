"""
Implement a Binary Tree with a list of lists.
"""

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
l = getLeftChild(r)
print('l', l)

setRootVal(l, 9)
print('r', r)
insertLeft(l, 11)
print('r', r)
print(getRightChild(getRightChild(r)))


def buildTree():
    r = BinaryTree('a')  # ['a', [], [] ]
    insertLeft(r, 'b')  # ['a', ['b', [], [] ], [] ]
    insertRight(r[1], 'd')
    insertRight(r, 'f')
    insertRight(r, 'c')
    insertLeft(r[2], 'e')
    print(r)

buildTree()
