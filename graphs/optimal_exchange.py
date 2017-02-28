# python3

class Graph:
    def __init__(self, n):
        self.n = n
        self.e = [ set([]) for _ in range(n + 1) ]
        self.ee = set([])

    def edge(self, u, v, w):
        self.e[u].add(v)
        self.ee.add((u, v, w))

    def optimal_path(self, s):
        (dist, cycled) = self.bellman_ford(s)
        visited = set([])
        for u in cycled:
            self.dfs(u, visited)

        return (dist, visited) 
    
    def dfs(self, n, visited):
        if n in visited:
            return
        visited.add(n)
        for u in self.e[n]:
            self.dfs(u, visited)

    def bellman_ford(self, s):
        dist = {s: 0}
        cycled = set([])
        for _ in range(self.n - 1):
            for e in self.ee:
                self.relax(e[0], e[1], e[2], dist)

        for e in self.ee:
            if self.relax(e[0], e[1], e[2], dist):
                cycled.add(e[1])
        return (dist, cycled)

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
    s = int(input())
    dist, cycled = g.optimal_path(s)
    for u in range(1, n + 1):
        if u not in cycled:
            if u not in dist:
                print('*')
            else:
                print(dist[u])
        else:
            print('-')

