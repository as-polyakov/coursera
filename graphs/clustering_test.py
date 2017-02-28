# python3
from random import *

def generate(k, n):
    f = open('clustering_test', 'w')
    f.write('{:d}\n'.format(n))
    points = set([])
    for _ in range(n):
        x, y = 0, 0
        while( (x, y) in points):
            x, y = randint(-1000, 1000), randint(-1000, 1000)
        f.write('{:d} {:d}\n'.format(x, y))
        points.add( (x, y) )
    f.write('{:d}\n'.format(k))
    f.close()

if __name__ == '__main__':
    n, k = map(int, input().split())
    generate(n, k)
