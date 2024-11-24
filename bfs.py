from collections import defaultdict


data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['M', 'N']
data['C'] = ['L']
data['D'] = ['O', 'P']
data['M'] = ['X', 'Y']
data['N'] = ['U', 'V']
data['O'] = ['I', 'J']
data['Y'] = ['R', 'S']
data['V'] = ['G', 'H']

class Node:
    def __init__(self, ten, cha=None):
        self.ten = ten
        self.cha = cha

def duongdi(n):
    print('tim thay duong di')
    path = []
    while n.cha != None:
        path.append(n.ten)
        n = n.cha
    path.append(n.ten)
    path.reverse()
    print('duong di: ', '->'.join(path))

def bfs(To, Tg):
    Mo = [To]
    Dong = []
    while True:
        if len(Mo) == 0:
            return print('Khong tim thay duong di')
        n = Mo.pop()
        if n.ten == Tg.ten:
            duongdi(n)
            return True
        Dong.append(n)
        pop = 0
        for v in data[n.ten]:
            tam = Node(v)
            if tam not in Mo and tam not in Dong:
                Mo.insert(pop, tam)
                pop += 1
                tam.cha = n

bfs(Node('A'), Node('U'))


