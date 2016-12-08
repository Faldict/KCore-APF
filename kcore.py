#!/usr/bin/env python

class KCore:
    '''
    The impletation of data structure
    '''
    def __init__(self):
        self.vertices = {}
        self.t = 0

    def addDoubleEdge(self, v1, v2):
        self.addSingleEdge(v1, v2)
        self.addSingleEdge(v2, v1)

    def addSingleEdge(self, src, dst):
        if src in self.vertices.keys():
            if dst not in self.vertices[src]:
                self.vertices[src].append(dst)
        else:
            self.vertices[src] = [dst]

    def prune(self, k):
        for v in self.vertices.keys():
            if len(self.vertices[v]) < k:
                del self.vertices[v]
        self.check()

    def check(self):
        for v in self.vertices.keys():
            for dst in self.vertices[v]:
                if dst not in self.vertices.keys():
                    del self.vertices[v].remove(dst)

    def evolve(self):
        hist = [len(self.vertices)]
        while True:
            self.prune()
            amount = len(self.vertices)
            if amount != hist[self.t]:
                self.t += 1
                hist[self.t] = amount
            else:
                return hist

