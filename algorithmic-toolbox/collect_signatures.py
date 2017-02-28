# python3

from collections import namedtuple
def min_signatures(a):
    a.sort(key = lambda x: x[1])
    n = 0
    r = a
    visits = []
    while(r):
        c = r[0]
        r = list(filter(lambda x: x[0] > c[1], r))
        n += 1
        visits.append(c[1])
    return Schedule(n, visits)



if __name__ == '__main__':
    Schedule = namedtuple('Schedule', ['n', 'visit'])
    n = int(input())
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().split())))
    s = min_signatures(a)
    print(s.n)
    print(' '.join(map(str, s.visit)))
