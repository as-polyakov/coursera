# python3
from random import *
from subprocess import *

M = 100000

def generate_graph():
    seed()
    f = open('test', 'w')
    n, m = randint(1, M), randint(0, M)
    f.write(' '.join((str(n), str(m))) + '\n')
    for _ in range(m):
        u, v = 0, 0
        while u == v:
            u, v = randint(1, n), randint(1, n)
        f.write(' '.join((str(u), str(v))) + '\n')
    f.close()


def test():
    f = open('test')
    v1 = check_output(['java', 'Bipartite'], stdin = f)
    f.seek(0)
    v2 = check_output(['python3', 'bipartite.py'], stdin = f)
    return v1 == v2

if __name__ == '__main__':
    n = 0
    p = True
    while(n < 1000 and p):
        generate_graph()
        print('generated, testing...')
        p = test()
        print('passed ' + str(n))
        n += 1
    if p:
        print('all passed')
