# python3
import sys

def min_coins(n, coins, mc):
    if n == 0:
        return 0
    if n in mc:
        return mc[n]
    min = -1
    for c in coins:
        if c > n:
            continue
        c_min = min_coins(n - c, coins, mc)
        if c_min >= 0 and (min > c_min + 1 or min < 0):
            min = c_min + 1
    mc[n] = min
    return min

if __name__ == '__main__':
    n = int(input())
    coins = list(map(int, input().split()))
    print(min_coins(n, coins, {}))
