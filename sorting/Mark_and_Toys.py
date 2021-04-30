def Merge(prices,l,mid,h):
    leftSideArray=prices[l:mid+1]
    rightSideArray=prices[mid+1:h+1]
    
    leftSidePointer=0
    rightSidePointer=0    
    k=l
    while(leftSidePointer<len(leftSideArray) and rightSidePointer<len(rightSideArray)):
        if(leftSideArray[leftSidePointer]>rightSideArray[rightSidePointer]):
            prices[k]=rightSideArray[rightSidePointer]
            rightSidePointer+=1
        else:
            prices[k]=leftSideArray[leftSidePointer]
            leftSidePointer+=1
        k+=1
        
    while(leftSidePointer<len(leftSideArray)):
        prices[k]=leftSideArray[leftSidePointer]
        leftSidePointer+=1
        k+=1
    
    while(rightSidePointer<len(rightSideArray)):
        prices[k]=rightSideArray[rightSidePointer]
        rightSidePointer+=1
        k+=1
            
    
def MergeSort(prices,l,h):
    if l<h:
        mid=(l+h)//2
        MergeSort(prices,l,mid)
        MergeSort(prices,mid+1,h)
        
        Merge(prices,l,mid,h)
        
def maximumToys(prices, k):
    # Write your code here
    MergeSort(prices,0,len(prices)-1)
    total=0
    count=0
    for i in prices:
        if total+i>k:
            break
        total+=i
        count+=1
    return count
