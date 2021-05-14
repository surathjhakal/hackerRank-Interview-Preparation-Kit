def isBalanced(s):
    # Write your code here
    a=[]
    d={")":"(","}":"{","]":"["}
    for i in s:
        if i in d:
            if len(a)<1:
                return "NO"
            p=a.pop()
            if p!=d[i]:
                return "NO"
        else:
            a.append(i)
      
    if len(a)<1:
        return "YES"
    else:
        return "NO"
