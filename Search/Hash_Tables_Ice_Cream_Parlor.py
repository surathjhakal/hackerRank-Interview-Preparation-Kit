def whatFlavors(cost, money):
    # Write your code here
    d={}
    n=len(cost)
    for i in range(n):
        if cost[i] in d:
            d[cost[i]]+=[i+1]            
        else:
            d[cost[i]]=[i+1]
    for i in cost:
        val=money-i
        curr=d[i][0]
        if val==i:
            d[val].pop(0)
        if val in d:
            if len(d[val])>0:
                print(curr,d[val][0])
                return
