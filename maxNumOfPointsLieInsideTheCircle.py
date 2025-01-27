def solution(S, X, Y):
    n = len(S)
    d = []
    for c, x, y in zip(S, X, Y):
        d.append((x**2+y**2), c)
    d.sort()
    ans = i = 0
    st = set()
    while i < n:
        j = i
        t = []
        p = set()
        while j < n and d[j][0] == d[i][0]:
            p.add(d[j][1])
            t.append(d[j][1])
            j += 1
        if len(p) != len(t):
            break
        else:
            ok = True
            for x in t:
                if x in st:
                    ok = False
            if ok:
                st |= p
                ans += len(p)
            else:
                break
        i = j
    return ans