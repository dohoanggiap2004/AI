

graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'F': 5, 'E': 12},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'Z': 5},
    'F': {'Z': 17},
}

h = {
    'A': 11,
    'B': 11,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 0,
    'Z': 0
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


def A_star(graph, start, goals, h):
    # Tập đỉnh mở (MO) bắt đầu với đỉnh khởi đầu
    MO = [start]
    # Tập đỉnh đóng (DONG) để lưu các đỉnh đã xét
    DONG = []
    # g lưu chi phí thực tế từ đỉnh bắt đầu đến mỗi đỉnh
    g = {start: 0}
    # f lưu giá trị f(n) = g(n) + h(n) cho mỗi đỉnh
    f = {start: h[start]}
    # parent lưu cha của mỗi đỉnh để truy ngược đường đi
    parent = {}

    while MO:
        # Tìm đỉnh n có giá trị f(n) nhỏ nhất trong tập MO
        min_f = float('inf')
        n = None
        for node in MO:
            if f[node] < min_f:
                min_f = f[node]
                n = node

        # Nếu n nằm trong tập đích (goals), kết thúc và in ra đường đi
        if n in goals:
            duongdi(start, n, g, parent)
            return True

        # Chuyển n từ tập MO sang DONG
        MO.remove(n)
        DONG.append(n)

        # Xét các đỉnh kề của n
        for neighbor, cost in graph.get(n, {}).items():
            cost_g_new = g[n] + cost  # Chi phí mới từ start đến neighbor

            if neighbor in g and cost_g_new < g[neighbor]:
                g[neighbor] = cost_g_new
                f[neighbor] = cost_g_new + h[neighbor]  # Thêm phần tính f(n) cho A*
                parent[neighbor] = n
            elif neighbor not in MO and neighbor not in DONG:
                g[neighbor] = cost_g_new
                f[neighbor] = cost_g_new + h[neighbor]  # Tương tự, thêm f(n)
                parent[neighbor] = n
                MO.append(neighbor)

    # Nếu không tìm thấy đường đi, thông báo
    print("Không tìm thấy đường đi")
    return False

start = 'A'
goals = {'Z'}
A_star(graph, start, goals, h)

