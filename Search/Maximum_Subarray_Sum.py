def maximumSum(arr, m):
    # Write your code here
    computed = []
    prevS = 0
    for i in range(n):
        prevS = (prevS + arr[i]) % m
        computed.append((prevS, i))

    minS = -1
    computed = sorted(computed)
    for i in range(n -1):
        if computed[i][1] > computed[i+1][1] and (minS == -1 or minS > computed[i+1][0] - computed[i][0]):
            minS = computed[i+1][0] - computed[i][0]
    return max(computed[n-1][0], m - minS)
