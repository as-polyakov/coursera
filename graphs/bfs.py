# python3

class UGraph:
    def __init__(self, n, m):
        self.e = [ set([]) for _ in range(n + 1) ]
    def edge(self, u, v):
        self.e[u].add(v)
        self.e[v].add(u)

    def bfs(self, u):
        q = []
        dist = {}
        processed = set([])
        q.append(u)
        d = 0
        while(len(q) > 0):
            i = len(q)
            for _ in range(i):
                v = q.pop(0);
                if v in processed:
                    continue
                dist[v] = d
                processed.add(v)
                q.extend(filter(lambda x: x not in processed, self.e[v]))
            d += 1
        return dist

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = UGraph(n, m)
    for _ in range(m):
        u, v = map(int, input().split())
        g.edge(u, v)
    u, v = map(int, input().split())
    dist = g.bfs(u)
    print(-1 if v not in dist else dist[v])
