# python3

class Graph:
    def __init__(self, n):
        self.verticies = {k: set([]) for k in range(1, n + 1)}
    def vertex(self, u, v):
        self.verticies[u].add(v)
    
    def contains_cycle(self):
        visited = {}
        for u in self.verticies:
            if u not in visited:
                n_visited = {}
                if self.dfs(n_visited, u):
                    return True
                visited.update(n_visited)
        return False

    def dfs(self, state, u):
        if u in state and state[u] == 1:
            return True
        if u in state and state[u] == 2:
            return False
        state[u] = 1
        for v in self.verticies[u]:
            if self.dfs(state, v):
                return True
        state[u] = 2
        return False

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        u, v = map(int, input().split())
        g.vertex(u, v)
    print(1 if g.contains_cycle() else 0)
