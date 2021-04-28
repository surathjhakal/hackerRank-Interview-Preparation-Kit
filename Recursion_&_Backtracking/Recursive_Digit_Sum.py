def superDigit(n, k):
    # Write your code here
    if len(n)==1:
        temp=str(int(n)*k)
        t=0
        for i in temp:
            t+=int(i)
        return t

    total=0
    for i in n:
        total+=int(i)
        
    return superDigit(str(total),k)
