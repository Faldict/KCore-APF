#!/usr/bin/env python
import time

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
                    self.vertices[v].remove(dst)

    def evolve(self, k):
        hist = [len(self.vertices)]
        while True:
            self.prune(k)
            amount = len(self.vertices)
            if amount != hist[self.t]:
                self.t += 1
                hist.append(amount)
            else:
                return hist


def main():
    filepath = "~/dfy/PATT/Author_Author_cs.txt"
    graph = KCore()
    fi = open(filepath, "r")
    print "Start running at %s" % time.ctime()
    count = 0
    while(count < 100000):
        line = fi.readline()[:-1]
        (v1, v2) = line.split('\t')
        graph.addDoubleEdge(v1, v2)
    fi.close()
    print "[INFO] Finish readfile at %s" % time.ctime()
    graph.check()
    print "[INFO] Start evolving at %s" % time.ctime()
    hist = graph.evolve(10)
    fo = open("kcore.txt", "a")
    for t in range(len(hist)):
        line = "%s\t%s\n" % (t, hist[t])
        fo.write(line)
    fo.close()
    print "[FINISH] Finish evolve at %s" % time.ctime()

if __name__ == '__main__':
    main()





