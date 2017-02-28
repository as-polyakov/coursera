# python3
from math import * 

class Graph:

    def __init__(self, n):
        self.n = n
        self.ee = set([])
        self.v = [None] * n
        self.p = [-1] * n

    def build(self):
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = (self.v[i][0] - self.v[j][0]) ** 2, (self.v[i][1] - self.v[j][1]) ** 2
                w = sqrt(a + b)
                self.edge(i, j, w)

    def vertex(self, n, x, y):
        self.v[n] = (x, y)

    def edge(self, u, v, w):
        self.ee.add((u, v, w))

    def min_total_weight(self):
        edges = sorted(self.ee, key = lambda x: x[2])
        w, n = 0, 0
        for edge in edges: 
            if n == self.n - 1:
                break
            if self.maybe_add(edge):
                w += edge[2]
        return w

    def maybe_add(self, edge):
        if self.find(edge[0]) != self.find(edge[1]):
           self.union(edge[0], edge[1])
           return True
        return False

    def union(self, i, j):
        ix = self.find(i)
        jx = self.find(j)
        self.p[jx] = ix

    def find(self, i):
        if(self.p[i] == -1):
            return i
        return self.find(self.p[i])

if __name__ == '__main__':
    n = int(input())
    g = Graph(n)
    for i in range(n):
        x, y = map(int, input().split())
        g.vertex(i, x, y)
    g.build()
    print('{:.9f}'.format(g.min_total_weight()))
