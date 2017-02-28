# python3
from functools import reduce

def revenue(a, b):
    a.sort()
    b.sort()
    return reduce(lambda x, y: x + y, map(lambda x: x[0] * x[1], zip(a, b)))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(revenue(a, b))
