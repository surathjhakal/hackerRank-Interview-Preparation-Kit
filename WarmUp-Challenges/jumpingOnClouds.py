# Complete the jumpingOnClouds function below.
#Complexity is time:O(n)(It takes less time but idk what is the Big O because its not log N) & space=O(1)
def jumpingOnClouds(c):
    count=0
    i=0
    jump=0
    while i<len(c)-1:
        if(len(c)-1)-i>1:
            if(c[i+2]==0):
                jump=1
            else:
                jump=0
        else:
            jump=0        
        i+=1
        i+=jump
        count+=1
    return count
