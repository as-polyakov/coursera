# python3
from subprocess import *
from random import *

def generate(n):
    seed()
    has_negative_cycle = random() > 0.5
    negative_weight = 0
    edges = [ set([]) for _ in range(n + 1) ]
    cycle_len = 0
    if(has_negative_cycle):
        (negative_weight, cycle_len) = add_cycle(edges, n)
        print('added cycle of len ' + str(cycle_len))
    m = randint(cycle_len, min(10000, n * n // 2))
    for _ in range(m - cycle_len):
        u, v = -1, -1
        while(u < 0 or v < 0 or contains(u, v, edges)):
            u, v = randint(1, n), randint(1, n)
        add_edge(u, v, edges, randint(1, 200))
    flush_graph(n, m, edges)
    return (has_negative_cycle, negative_weight)

def contains(u, v, edges):
    for vv in edges[u]:
        if vv[0] == v:
            return True
    return False

def add_cycle(edges, n):
    start = randint(1, n)
    p = start
    l = randint(0, n - 2)
    used = set([start])
    weight = 0
    print('adding cycle')
    v = start
    for _ in range(l):
        while(v in used):
            v = randint(1, n)
        used.add(v)
        w = randint(-200, 200)
        print(p, v, w)
        weight += w
        add_edge(p, v, edges, w)
        p = v
    add_edge(v, start, edges, -weight - 1)
    weight += -weight - 1
    return (weight, len(used))

def add_edge(u, v, edges, w):
    edges[u].add((v, w))

def flush_graph(n, m, edges):
    f = open('test_anomalies', 'w')
    f.write('{:d} {:d}\n'.format(n, m))
    for u in range(1, n + 1):
        for vw in edges[u]:
            f.write('{:d} {:d} {:d}\n'.format(u, vw[0], vw[1]))
    f.close()

def test(expected):
    f = open('test_anomalies')
    #v1 = check_output(['java', 'Bipartite'], stdin = f)
    f.seek(0)
    v2 = check_output(['python3', 'anomalies.py'], stdin = f)
    return int(v2) == expected

if __name__ == '__main__':
    eq = True
    while(eq):
        (has_negative_cycle, negative_weight) = generate(1000)
        print('generated', (has_negative_cycle, negative_weight))
        eq = test(has_negative_cycle)
    print('found')

