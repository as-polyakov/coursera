#python3

def fib(n):
    a, b, i = 0, 1, 1
    if n < 2:
        return a if n == 0 else b
    while(i < n):
        a, b = b, a + b
        i += 1
    return b

if __name__ == '__main__':
    print(fib(int(input())))
