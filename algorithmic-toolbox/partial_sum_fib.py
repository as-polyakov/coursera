# python3

def pisano(n):
    a, b, i = 0, 1, 1
    while(not (a == 0 and b == 1 and i > 2)):
        a, b = b, (a + b) % n
        i += 1
    return i - 1

def fib(n, m):
    a, b, i = 0, 1, 1
    p = pisano(m)
    if n < 2:
        return a % m if n == 0 else b % m
    for i in range(2, (n + 1) % p):
        a, b = b, (a + b) % m
    return b

if __name__ == "__main__":
    m, n = map(int, input().split())
    print( (fib(n + 2, 10) - fib(m + 1, 10)) % 10)
