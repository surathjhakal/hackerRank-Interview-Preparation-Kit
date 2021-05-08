def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    m=arr[-1]-arr[0]
    for i in range(1,n):
        if arr[i]-arr[i-1]<m:
            m=arr[i]-arr[i-1]
    return m
