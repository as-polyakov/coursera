# python3

import resource
import sys

sys.setrecursionlimit(10000)

class Graph:
    def __init__(self, n):
        self.n = n
        self.ee = set([])

    def edge(self, u, v, w):
        self.ee.add((u, v, w))

    def has_negative_cycle(self):
        relaxed = set([])
        for s in range(1, n + 1):
            if s in relaxed:
                continue
            if self.bellman_ford(s, relaxed):
                return True
        return False

    def bellman_ford(self, s, relaxed):
        dist = {s: 0}
        relaxed.add(s)
        for _ in range(self.n - 1):
            for e in self.ee:
                if self.relax(e[0], e[1], e[2], dist):
                    relaxed.add(e[1])

        for e in self.ee:
            if self.relax(e[0], e[1], e[2], dist):
               return True
        return False

    def relax(self, u, v, w, dist):
        if u not in dist:
            return False
        if v not in dist or dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            return True
        return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v, w = map(int, input().split())
        g.edge(u, v, w)
    print(1 if g.has_negative_cycle() else 0)

