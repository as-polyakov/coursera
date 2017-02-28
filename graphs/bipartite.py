# python3

from sys import setrecursionlimit


class UGraph:
    def __init__(self, n, m):
        self.e = [ set([]) for _ in range(n + 1) ]

    def edge(self, u, v):
        self.e[u].add(v)
        self.e[v].add(u)
    
    def is_bipartite(self):
        processed = set([])
        for v in range(1, n + 1):
            if v not in processed:
                if not self.is_bipartite_sub(v, processed):
                    return False
        return True

    def is_bipartite_sub(self, u, processed):
        st = [u]
        colors = {u: False}
        while len(st) > 0:
            u = st.pop()
            if u in processed:
                continue
            c = colors[u]
            processed.add(u)
            for v in self.e[u]:
                if v in colors and colors[v] != (not c):
                    return False
                else:
                    colors[v] = (not c)
                st.append(v)
        return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    g = UGraph(n, m)
    for _ in range(m):
        u, v = map(int, input().split())
        g.edge(u, v)
    print(1 if g.is_bipartite() else 0)
