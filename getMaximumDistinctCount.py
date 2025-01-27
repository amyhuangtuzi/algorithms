from collections import Counter

def getMaximumDistinctCount(a, b, k):
    count_a = Counter(a)
    d = len(count_a)
    s = sum(v - 1 for v in count_a.values())
    set_a = set(count_a.keys())
    P = set()

    for num in b:
        if num not in set_a:
            P.add(num)
    t = len(P)

    return d + min(s, k, t)
