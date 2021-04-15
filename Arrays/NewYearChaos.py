# Complete the minimumBribes function below.

# The complexity of program is time: O(n) and space: O(1)
def swap(arr,i1,i2):
    temp=arr[i1]
    arr[i1]=arr[i2]
    arr[i2]=temp

def minimumBribes(q):
    chaotic=False
    count=0
    for i in range(len(q)-1,-1,-1):
        if(q[i]!=i+1):
            if(q[i-1]==i+1):
                count+=1
                swap(q,i,i-1)
            elif(q[i-2]==i+1):
                count+=2
                swap(q,i,i-1)
                swap(q,i,i-2)
            else:
                chaotic=True
                break
    if chaotic:
        print("Too chaotic")
    else:
        print(count)
