def solution(U, L, C):
    if U + L != sum(C):
        return "IMPOSSIBLE"
    n = len(C)
    a = [[0] * n for _ in range(2)]
    for i in range(n):
        if C[i] == 2:
            a[0][i] = a [1][i] =1
            U -= 1
            L -= 1
        elif C[i] == 1:
            if U:
                a[0][i] = 1
                U -= 1
            elif L:
                a[1][i] = 1
                L -= 1
    s = []
    for i in range(2):
        for j in range(n):
            s.append(str(a[i][j]))
        if i == 0:
            s.append(',')

    return "".join(s)

