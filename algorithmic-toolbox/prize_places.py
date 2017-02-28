# python3
from collections import namedtuple

def partition(n):
    c, m = 1, 1
    part = set([])
    while(n > 0):
        if n - c > m and n - c != c:
            n -= c
            part.add(c)
            m = c
            c += 1
        else:
            part.add(n)
            break
    return part


if __name__ == '__main__':
    n = int(input())
    res = partition(n)
    print(len(res))
    print(' '.join(map(str, res)))

