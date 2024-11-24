from sys import flags
from turtledemo.penrose import start

graph = {
    'A': {'B': 2, 'C': 4, 'F': 6},
    'B': {},
    'C': {'D': 2, 'E': 8},
    'D': {'E': 2},
    'E': {},
    'F': {'G': 5},
    'G': {},
    'H': {}
}

def duongdi(start, goal, g, parent):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = parent[curr]
    path.append(start)
    path.reverse()
    print('duong di:', ' -> '.join(path))
    print('C[p] = ', g[goal])

def at(start, goals, graph):
    MO = [start]
    DONG = []
    parent = {}
    g = {start: 0}
    while MO:
        minCost = float('inf')
        n = None
        for v in MO:
            if v in g:
                cost = g[v]
            else:
                cost = float('inf')
            if cost < minCost:
                minCost = cost
                n = v

        if n in goals:
            duongdi(start, n, g, parent)
            return True

        MO.remove(n)
        DONG.append(n)

        for neightbor, cost in graph.get(n, {}).items():
            newCost = g[n] + cost
            if neightbor in g and newCost < g[neightbor]:
                g[neightbor] = newCost
                parent[neightbor] = n
            elif neightbor not in MO and neightbor not in DONG:
                g[neightbor] = newCost
                parent[neightbor] = n
                MO.append(neightbor)

start = 'A'
goals = {'E', 'H'}
at(start, goals, graph)

