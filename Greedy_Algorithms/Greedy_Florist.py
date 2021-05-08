def getMinimumCost(k, c):
    c.sort()
    total=0
    person={}
    n=len(c)
    j=1
    for i in range(1,k+1):
        person[i]=0
    for i in range(n-1,-1,-1):
        if j==k+1:
            j=1
        person[j]+=1
        total+=c[i]*person[j]
        j+=1
    return total
