# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
#Complexity is time:O(n) & space=O(1)
def countingValleys(steps, path):
    # Write your code here
    valleyCount=0
    seaPoint=0
    for path in path:
        if path=='U':
            seaPoint+=1
            if seaPoint==0:
                valleyCount+=1
        else:
            seaPoint-=1
    return valleyCount
