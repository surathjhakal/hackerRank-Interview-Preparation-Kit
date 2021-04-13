# Complete the repeatedString function below.
def count(s,c):
    return s.count(c)

# The complexity of this program is time:O(logn) and space:O(1)
def repeatedString(s, n):
    d=n//len(s)
    c=count(s,'a')
    c*=d
    diff=n-(len(s)*d)
    c+=count(s[:diff],'a')
    return c
