"""
Implement a binary tree with Nodes and references.
"""


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left= None
        self.right= None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def setRoot(self, obj):
        self.key = obj

    def getRoot(self):
        return self.key


def buildTree():
    r = BinaryTree('a')
    r.insertLeft('b')
    r.getLeft().insertRight('d')
    r.insertRight('f')
    r.insertRight('c')
    r.getRight().insertLeft('e')
    return r


buildTree()
