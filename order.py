from collections import deque

def order(city_nodes, city_from, city_to, company):
    adjacency = [[] for _ in range(city_nodes + 1)]
    for f, t in zip(city_from, city_to):
        adjacency[f].append(t)
        adjacency[t].append(f)
    d = [-1] * (city_nodes + 1)
    queue = deque([company])
    d[company] = 0
    while queue:
        current = queue.popleft()
        for neighbour in adjacency[current]:
            if d[neighbour] == -1:
                d[neighbour] = d[current] + 1
                queue.append(neighbour)
    res = []
    for i in range(1, city_nodes + 1):
        if i != company and d[j] != -1:
            res.append(i)
    res.sort(key=lambda x: (d[x], x))

    return res