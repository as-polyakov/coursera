# python3

def knapsack(n, W, w):
    if n == 0 or W == 0:
        return 0

    if cache[n][W] != -1:
        return cache[n][W]
    if W - w[n - 1] >= 0:
        cache[n][W] = max(knapsack(n - 1, W, w), w[n - 1] + knapsack(n - 1, W - w[n - 1], w))
    else:
        cache[n][W] = knapsack(n - 1, W, w)
    return cache[n][W]

if __name__ == '__main__':
    W, n = map(int, input().split())
    cache = [[-1] * (W + 1) for _ in range(n + 1)]
    w = list(map(int, input().split()))
    print(knapsack(n, W, w))
