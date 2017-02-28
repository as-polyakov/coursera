# python3

class Graph:
    verticies = {}
    def add(self, u, v):
        if u in self.verticies:
            self.verticies[u].append(v)
        else:
            self.verticies[u] = [v]

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
    maze = Graph()
    for _ in range(m):
        u, v = map(int, input().split())
        maze.add(u, v)
        maze.add(v, u)
    u, v = map(int, input().split())
    print(1 if maze.is_connected(u, v) else 0)

