def findNumOfPairs(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    cnt = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            cnt += 1
            i += 1
            j += 1
        else:
            i += 1
    return cnt

