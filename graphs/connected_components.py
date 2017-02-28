# python3

class Graph:
    verticies = {}
    def __init__(self, n):
        for i in range(1, n + 1):
            self.verticies[i] = set([])

    def add(self, u, v):
        self.verticies[u].add(v)

    def num_components(self):
        visited = set([])
        n = 0
        for u in self.verticies:
            if u not in visited:
                n += 1
                n_visited = set([])
                self.dfs(u, n_visited)
                visited = visited.union(n_visited)
        return n

    def is_connected(self, a, b):
        visited = set([])
        self.dfs(a, visited)
        return b in visited

    def dfs(self, a, visited):
        if a in visited:
            return
        visited.add(a)
        if a not in self.verticies:
            return
        for v in self.verticies[a]:
            self.dfs(v, visited)


if __name__ == '__main__':
    n, m = map(int, input().split())
    maze = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        maze.add(u, v)
        maze.add(v, u)
    print(maze.num_components())

