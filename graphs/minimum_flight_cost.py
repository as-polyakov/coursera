# python3
from heapq import *

class HeapEntry:
    def __init__(self, n, val):
        self.n = n
        self.val = val
        self.removed = False

    def remove(self):
        self.removed = True

    def __lt__(self, other):
        return self.val < other.val

class Graph:
    def __init__(self, n, m):
        self.e = [set([]) for _ in range(n + 1)]
        self.n = n
    def edge(self, u, v, w):
        self.e[u].add((v, w))

    def min_cost(self, u, v):
        min_dist = []
        hu = HeapEntry(u, 0)
        heap_entries = {u: hu}
        q = []
        heappush(q, hu)
        dist = {u: 0}
        while(len(q) > 0):
            hv = q.pop(0)
            if hv.removed:
                continue
            for vv in self.e[hv.n]:
                if vv[0] not in dist or dist[vv[0]] > dist[hv.n] + vv[1]:
                    dist[vv[0]] = dist[hv.n] + vv[1]
                    if vv[0] in heap_entries:
                        heap_entries[vv[0]].remove()
                    heap_entries[vv[0]] = HeapEntry(vv[0], dist[vv[0]])
                    heappush(q, heap_entries[vv[0]])
        return dist[v] if v in dist else -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n, m)
    for _ in range(m):
        u, v, w = map(int, input().split())
        g.edge(u, v, w)
    u, v = map(int, input().split())
    print(g.min_cost(u, v))
    

