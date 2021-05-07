def countTriplets(arr, r):
    total=0
    left={}
    right={}
    n=len(arr)
    for i in arr:
        if i in right:
            right[i]+=1
        else:
            right[i]=1
    for i in range(n):
        curr=arr[i]
        right[curr]-=1
        lVal=0
        if curr%r==0:
            lVal=curr//r
        rVal=curr*r
        
        if lVal not in left and curr not in left:
            left[curr]=1
            continue
        if lVal not in left and curr in left:
            left[curr]+=1
            continue
        lfreq=left[lVal]
        
        if rVal not in right:
            continue
        else:
            rfreq=right[rVal]
        
        total+=lfreq*rfreq
        if curr not in left:
            left[curr]=1
        else:
            left[curr]+=1
            
    return total
