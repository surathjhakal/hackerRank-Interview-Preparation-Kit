def largestRectangle(h):
    # Write your code here
    h=h+[0]
    stack = []
    i = 0
    best = 0
    while i<=n:
        if len(stack)==0 or h[stack[-1]]<=h[i]:
            stack.append(i)
            i+=1
        else:
            print(stack)
            print("second",i)
            p = stack.pop()
            A = h[p]*(i-stack[-1]-1) if len(stack)>0 else h[p]*i
            print(A)
            best = max(best,A)
    return best
