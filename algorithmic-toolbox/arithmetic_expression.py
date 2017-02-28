# python3
from re import split

class Node:
    def __init__(self, v):
        self.v = v
        self.p = None
        self.n = None



def max_value(operands, operators):
    permutations = []
    permutate([False] * len(operators), [], permutations, len(operators))
    m = calc(operands, operators, permutations[0])
    for i in range(1, len(permutations)):
        mi = calc(operands, operators, permutations[i])
        m = m if m > mi else mi
    return m

def permutate(used, res, permutations, n):
    if len(res) == n:
        permutations.append(res[:])
        return
    for i in range(len(used)):
        if not used[i]:
            used[i] = True
            res.append(i)
            permutate(used, res, permutations, n)
            res.pop()
            used[i] = False
    return

def print_list(st):
    res = []
    while(st != None):
        res.append(st.v)
        st = st.n
    print('list: ', res)

def calc(operands, operators, order):
    st = []
    ops = [None] * len(operators) 
    prev = None
    for i in range(len(operators)):
        op1 = Node(operands[i]) if prev == None else prev
        op2 = Node(operands[i + 1])
        o = Node(action(operators[i]))
        ops[i] = o
        if prev != None:
            prev.n = o
        op1.p = prev
        op1.n = o
        o.p = op1
        o.n = op2
        op2.p = o
        op2.n = None
        prev = op2
    l = ops[0].p
    for i in order:
        o = ops[i]
        
        o.p.v = o.v(o.p.v, o.n.v)
        nn = o.n.n
        if nn != None:
            nn.p = o.p
        o.p.n = nn
    return l.v
def action(a):
    s = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
    }
    return s.get(a)

def parse(s):
    s = split("([+-/*])", s)
    is_operator = lambda x: x in ("*", "/", "-", "+", s)
    return (list(map(int, filter(lambda x: not is_operator(x), s))), 
        list(filter(is_operator, s)))

if __name__ == '__main__':
    (operands, operators) = parse('5-8+7*4-8+9')
    print(max_value(operands, operators))
    #print(calc(operands, operators, [4, 3, 1, 0, 2]))

