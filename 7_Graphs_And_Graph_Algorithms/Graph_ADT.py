"""
Implement the Graph Abstract Data Type
"""

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, target):
        if target in self.vertList:
            return self.vertList[target]
        else:
            return None

    def __contains__(self, target):
        return target in self.vertList

    def addEdge(self, frm, to, cost=0):
        if frm not in self.vertList:
            newVertex = addVertex(frm)
        if to not in self.vertList:
            newVertex = addVertex(to)
        self.vertList[frm].addNeighbour(self.vertList[to], cost)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
