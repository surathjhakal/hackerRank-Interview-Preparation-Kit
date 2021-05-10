def pairs(k, arr):
    # Write your code here
    count=0
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    # print(d)
    for i in arr:
        # print(i,count)
        if i-k in d:
            count+=d[i-k]
    return count
