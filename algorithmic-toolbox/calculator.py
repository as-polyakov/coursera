# python3
import sys

sys.setrecursionlimit(1000000)

def min3(a, b, c):
    return min(a, min(b, c))

def min_ops(n):
    if cache[n] != -1:
        return cache[n];
    if n % 2 == 0 and n % 3 == 0:
        cache[n] = 1 + min3(min_ops(n // 2), min_ops(n // 3), min_ops(n - 1))
    elif n % 2 == 0:
        cache[n] = 1 + min(min_ops(n // 2), min_ops(n - 1))
    elif n % 3 == 0:
        cache[n] = 1 + min(min_ops(n // 3), min_ops(n - 1))
    else:
        cache[n] = 1 + min_ops(n - 1)
    return cache[n]

def min_ops_iterative(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            cache[i] = 1 + min3(cache[i // 2], cache[i // 3], cache[i - 1])
        elif i % 2 == 0:
            cache[i] = 1 + min(cache[i // 2], cache[i - 1])
        elif i % 3 == 0:
            cache[i] = 1 + min(cache[i // 3], cache[i - 1])
        else:
            cache[i] = 1 + cache[i - 1]
    return cache[n]

def reconstruct(n, ops):
    while(n > 0):
        ops.append(n)
        if n % 2 == 0 and n % 3 == 0:
            m = min3(cache[n // 2], cache[n // 3], cache[n - 1]) 
            if m == cache[n // 2]:
                n //= 2
            elif m == cache[n // 3]:
                n //= 3
            else:
                n -= 1
        elif n % 2 == 0:
            m = min(cache[n // 2], cache[n - 1])
            if m == cache[n // 2]:
                n //= 2
            else:
                n -= 1
        elif n % 3 == 0:
            m = min(cache[n // 3], cache[n - 1])
            if m == cache[n // 3]:
                n //= 3
            else:
                n -= 1
        else:
            n -= 1
    ops.reverse()

if __name__ == '__main__':
    n = int(input())
    cache = [-1] * (n + 1)
    cache[1] = 0
    ops = []
    print(min_ops_iterative(n))
    reconstruct(n, ops)
    print(' '.join(map(str, ops)))
