#python3

def fib_last_digit(n):
    a, b = 0, 1
    if n < 2:
        return a if n == 0 else b
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b

if __name__ == '__main__':
    print(fib_last_digit(int(input())))
