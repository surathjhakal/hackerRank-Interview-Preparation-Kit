# Complete the rotLeft function below.
# The complexity of program is time: O()? and space: O(1)
def rotLeft(a, d):
    n=len(a)
    l=n-d
    b=a[-1:(l*-1)-1:-1]
    for i in b:
        a.insert(0,i)
    a=a[:n:]
    return a
