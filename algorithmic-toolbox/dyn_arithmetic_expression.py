# python3
from re import split

def max4(a, b, c, d):
    return max(max(a, b), max(c, d))

def min4(a, b, c, d):
    return min(min(a, b), min(c, d))

def optimal_max(d, op):
    return optimal(d, op, 0, len(d) - 1, max4, cache_M)


def optimal(d, op, i, j, maxmin, cache):
    if i == j:
        cache[i][j] = d[i]
        return d[i]
    if cache[i][j] != None:
        return cache[i][j]
    opt = None
    for k in range(i, j):
        m = maxmin(
                op[k](optimal(d, op, i, k, max4, cache_M), optimal(d, op, k + 1, j, max4, cache_M)),
                op[k](optimal(d, op, i, k, max4, cache_M), optimal(d, op, k + 1, j, min4, cache_m)),
                op[k](optimal(d, op, i, k, min4, cache_m), optimal(d, op, k + 1, j, min4, cache_m)),
                op[k](optimal(d, op, i, k, min4, cache_m), optimal(d, op, k + 1, j, max4, cache_M))
                )
        opt = m if opt == None else maxmin(m, opt, opt, opt)
    cache[i][j] = opt
    return opt

def parse(s):
    tok = split("([+-/*])", s)
    o = { 
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '/': lambda x, y: x / y,
            '*': lambda x, y: x * y
    }
    (d, op) = list(map(int, filter(lambda x: x.isdigit(), tok))), list(map(lambda x: o[x], filter(lambda x: not x.isdigit(), tok)))
    return (d, op)

def reconstruct_solution(i, j, sol):
    m, mk = None, None
    if i == j:
        return
    for k in range(i, j):
        mm = max4(
                op[k](cache_M[i][k], cache_M[k + 1][j]),
                op[k](cache_m[i][k], cache_M[k + 1][j]),
                op[k](cache_m[i][k], cache_m[k + 1][j]),
                op[k](cache_M[i][k], cache_m[k + 1][j])
                )
        if m == None or m < mm:
            m = mm
            mk = k
    sol.append(mk)
    print(mk)
    reconstruct_solution(i, mk, sol)
    reconstruct_solution(mk + 1, j, sol)

if __name__ == '__main__':
    (d, op) = parse('5-8+7*4-8+9')    
    #(d, op) = parse('1-2+3*4')
    cache_M = [[None] * len(d) for _ in range(len(d))]
    cache_m = [[None] * len(d) for _ in range(len(d))]
    print(optimal_max(d, op))
    sol = []
    reconstruct_solution(0, len(d) - 1, sol)
    print(sol)
