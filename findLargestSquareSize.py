def findLargestSquareSize(samples):
    if not samples or not samples[0]:
        return 0

    n = len(samples)
    dp = [[0] * n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if sampels[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            else:
                dp[i][j] = 0

    return ans