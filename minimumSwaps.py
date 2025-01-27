def minimumSwaps(p):

    ip = [(v, i) for v, i in enumerate(p)]
    ip.sort(key=lambda  x: x[0], reverse=True)
    n = len(p)
    vis = [False] * n
    swaps = 0
    for i in range(n):
        if vis[i] or ip[i][1] == i:
            continue
        c = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = ip[j][1]
            c += 1
        if c > 1:
            swaps += (c-1)
    return swaps