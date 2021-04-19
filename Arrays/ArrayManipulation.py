def arrayManipulation(n, queries):
    arr=[0]*(n+2)
    for a,b,k in queries:
        arr[a]+=k
        arr[b+1]-=k
        
    maxi=temp=0
    for val in arr:
        temp+=val
        maxi=max(maxi,temp)
    
    return maxi
