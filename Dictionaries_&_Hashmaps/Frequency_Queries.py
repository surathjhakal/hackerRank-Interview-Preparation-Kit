def freqQuery(queries):
    o=[]
    v={}
    d={}
    n=len(queries)
    for i in range(n):
        q=queries[i][0]
        val=queries[i][1]
        
        if q==1:
            if val in d:
                v[d[val]]-=1
                d[val]+=1
            else:
                d[val]=1
        elif q==2:
            if val in d:
                if d[val]>0:
                    v[d[val]]-=1
                    d[val]-=1
        else:
            if val in v:
                if v[val] > 0:
                    o.append(1)
                else:
                    o.append(0)
            else:
                o.append(0)
        if q!=3 and val in d:
            if d[val] not in v:
                v[d[val]]=1
            else:
                v[d[val]]+=1
    return o  
