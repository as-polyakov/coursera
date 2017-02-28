# python3

class Graph:
    def __init__(self, n):
        self.vert = {k: set([]) for k in range(1, n + 1) }
    
    def vertex(self, u, v):
        self.vert[u].add(v)

    def toposort(self):
        visited = {}
        l = []
        for u in self.vert:
            if not self.dfs(visited, l, u):
                return []
        return l
    
    def dfs(self, visited, l, u):
        if u in visited and visited[u] == 1:
            return False
        if u in visited and visited[u] == 2:
            return True
        visited[u] = 1
        for v in self.vert[u]:
            if not self.dfs(visited, l, v):
                return False
        visited[u] = 2
        l.insert(0, u)
        return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.vertex(u, v)
    print(' '.join(map(str, g.toposort())))
            

