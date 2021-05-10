def maxMin(k, arr):
    # Write your code here
    arr.sort()
    mini = 1000000000
    for i in range(len(arr)-k+1):
        diff=arr[i+k-1]-arr[i]
        if(diff<mini):
            mini=diff
    return mini
