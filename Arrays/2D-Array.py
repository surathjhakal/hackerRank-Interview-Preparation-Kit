# Complete the hourglassSum function below.
# The complexity of this progam is time: O(n^2) & space=O(1)
def hourglassSum(arr):
    maximum=-10000
    l=len(arr)
    for i in range(l-2):
        for j in range(l-2):
            U=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            M=arr[i+1][j+1]
            L=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            total=U+M+L
            if(total>maximum):
                maximum=total
    return maximum
