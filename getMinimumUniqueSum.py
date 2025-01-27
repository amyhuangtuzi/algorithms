def getMinimumUniqueSum(arr):
    arr.sort()
    prev = arr[0]
    ans = prev

    for i in range(1, len(arr)):
        curr = arr[i]
        if curr <= prev:
            curr = prev + 1
        prev = curr
        ans += curr

    return ans