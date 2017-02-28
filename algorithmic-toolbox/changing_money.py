# python3


def num_coins(n):
    c = 0
    c = c + n // 10
    n = n - 10 * (n // 10)
    c = c + n // 5
    n = n - 5 * (n // 5)
    c = c + n // 1
    n = n - 1 * (n // 1)
    return c

if __name__ == '__main__':
    print(num_coins(int(input())))
