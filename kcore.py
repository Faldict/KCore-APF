#!/usr/bin/env python

import time

edges = {}
points = {}


def addEdge(p1, p2):
    if p1 in edges.keys():
        edges[p1].append(p2)
    else:
        edges[p1] = [p2]
    if p2 in edges.keys():
        edges[p2].append(p1)
    else:
        edges[p2] = [p1]
    if p1 in points.keys():
        points[p1] += 1
    else:
        points[p1] = 1
    if p2 in points.keys():
        points[p2] += 1
    else:
        points[p2] = 1


def aveDegree():
    n = len(points)
    s = sum(points.values())
    return float(s) / float(n)


def prune(kcore):
    for k, v in edges:
        if v < kcore:
            for p in edges[k]:
                if p in points.keys():
                    points[p] -= 1
            del points[k]


def evolve(kcore):
    n = len(points)
    prune(kcore)
    while len(points) != n:
        n = len(points)
        prune(kcore)


def createTable():
    filename = "~/dfy/DM/Author_Author_dm.txt"
    try:
        file_object = open(filename, "r")
        print "[INFO] Start running at %s" % time.ctime()
        for line in file_object:
            line = line[:-1]
            (p1, p2) = line.split('\t')
            addEdge(p1, p2)
    finally:
        file_object.close()
        print "[INFO] Finish read data at %s" % time.ctime()


def main():
    createTable()
    result = []
    for k in range(0, 500, 50):
        evolve(k)
        result.append((k, aveDegree()))
    filename = "kcore_dm.txt"
    f = open(filename, "w")
    for res in result:
        f.write("%s\t%s\n" % res)
    f.close()
    print "[SUCCESS] Finish all!"


if __name__ == '__main__':
    main()
