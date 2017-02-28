# python3

def pisano(m):
    if m == 1:
        return 1
    a, b, i = 0, 1, 1
    while(not (a == 0 and b == 1 and i > 2) ):
        a, b = b, (a + b) % m
        i += 1
    return i - 1

def fib_modulo(n, m):
    p = pisano(m)
    return fib(n % p, m)
    
def fib(n, m):
    a, b, i = 0, 1, 1
    if n < 2:
        return a if n == 0 else b
    for i in range(2, n + 1):
        a, b = b, (a + b) % m
    return b

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fib_modulo(n, m))
    

