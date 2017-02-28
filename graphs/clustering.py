# python3
from math import *
from array import *

class Graph:

    def __init__(self, n):
        self.n = n
        self.v = [-1] * n
        self.ee = [] 
        self.e = [ set([]) for _ in range(n) ]
    
    def add_vertex(self, i, x, y):
        self.v[i] = (x, y)

    def add_edge(self, u, v, w, connect):
        self.ee.append((u, v, w))
        if False and connect:
            self.e[u].add(v)
            self.e[v].add(u)

    def build(self, connect):
        for v in range(self.n - 1):
            for u in range(v + 1, self.n):
                self.add_edge(u, v, sqrt((self.v[u][0] - self.v[v][0]) ** 2 + (self.v[u][1] - self.v[v][1]) ** 2), connect)

    def min_d(self, k):
        #if k > n // 2:
        return self.min_d_connect(k)
        #return self.min_d_disconnect(k)

    def min_d_disconnect(self, k):
        self.ee = sorted(self.ee, key = lambda x: x[2], reverse = True)
        idx, kk, edge = 0, 1, self.ee[0]
        while(kk < k):
            edge = self.ee[idx]
            self.e[edge[0]].remove(edge[1]) 
            self.e[edge[1]].remove(edge[0]) 
            kk = self.num_cc(self.e)
            idx += 1
        return edge[2]

    def min_d_connect(self, k):
        self.ee = sorted(self.ee, key = lambda x: x[2])
        idx, kk, edge = 0, self.n, self.ee[0]
        while(kk >= k):
            edge = self.ee[idx]
            self.e[edge[0]].add(edge[1]) 
            self.e[edge[1]].add(edge[0]) 
            kk = self.num_cc(self.e)
            idx += 1
        return edge[2]


    def num_cc(self, adj):
        visited = set([])
        res = 0
        for u in range(self.n):
            if self.dfs(u, adj, visited):
                res += 1
        return res

    def dfs(self, n, adj, visited):
        if n in visited:
            return False
        visited.add(n)
        for u in adj[n]:
            self.dfs(u, adj, visited)
        return True

if __name__ == '__main__':
    n = int(input())
    g = Graph(n)
    for i in range(n):
        x, y = map(int, input().split())
        g.add_vertex(i, x, y)
    k = int(input())
    g.build(k <= n // 2)
    print('{:.12f}'.format(g.min_d(k)))


