# python3

def majority(a, l, h):
    print(l, h)
    if h == l:
        return True
    if h - l == 1:
        return a[l] == a[h]
    n = (l + h) // 2
    if n - l > h - n - 1:
        return majority(a, l, n)
    elif n - l < h - n - 1:
        return majority(a, n + 1, h)
    return majority(a, l, n) and majority(a, n + 1, h)

def linear_majority(a):
    fr = {}
    for i in a:
        fr[i] = fr[i] + 1 if i in fr else 1
    for k in fr:
        if fr[k] > len(a) // 2:
            return True
    return False

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    #print(1 if majority(a, 0, len(a) - 1) else 0)
    print(1 if linear_majority(a) else 0)
