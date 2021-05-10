def getCount(arr,k):
    low=0
    high=len(arr)-1
    count=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=k:
            count=mid
            low=mid+1
        else:
            high=mid-1
    return count
def triplets(a, b, c):
    count=0
    a=sorted(list(set(a)))
    b=sorted(list(set(b)))
    c=sorted(list(set(c)))
    for i in b:
        a1=getCount(a,i)+1
        c1=getCount(c,i)+1
        count+=a1*c1
    return count
