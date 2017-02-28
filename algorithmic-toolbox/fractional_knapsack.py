# python3

def fractional_knapsack(W, items):
    val = 0
    items.sort(key = lambda t: t[0] / t[1], reverse = True)
    it, r = iter(items), W
    while(r > 0):
        item = next(it, None)
        if item == None:
            break
        w = item[1] if item[1] <= r else r
        val += w * item[0] / item[1]
        r -= w
    return val
        


if __name__ == '__main__':
    n, W = map(int, input().split())
    items = []
    for i in range(0, n):
        v, w = map(int, input().split())
        items.append( (v, w))
    print('{0:.4f}'.format(fractional_knapsack(W, items)))

