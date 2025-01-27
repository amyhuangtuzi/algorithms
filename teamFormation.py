def teamFormation(score, team_size, k):
    ans = 0
    for _ in range(team_size):
        n = len(score)
        if n <= k:
            mv = max(score)
            i = score.index(mv)
        else:
            f = score[:k]
            b = score[n - k:]
            fm = max(f)
            bm = max(b)
            if fm >= bm:
                i = f.index(fm)
            else:
                li = b.index(bm)
                i = (n - k) + li
        ans += socre[i]
        score.pop(i)

    return ans