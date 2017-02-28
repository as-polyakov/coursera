# python3

def binary_search(a, l, h, x):
    if l > h:
        return -1
    n = (h + l) // 2
    if a[n] == x:
        return n
    return binary_search(a, l, n - 1, x) if a[n] > x else binary_search(a, n + 1, h, x)

if __name__ == '__main__':
    a = list(map(int, input().split()))
    n = a.pop(0)
    b = list(map(int, input().split()))
    k = b.pop(0)
    a.sort()
    res = []
    for i in range(k):
        res.append(binary_search(a, 0, len(a) - 1, b[i]))
    print(' '.join(map(str, res)))
