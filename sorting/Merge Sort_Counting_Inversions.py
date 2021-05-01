def Merge(arr,l,mid,h):
    total=0
    leftArr=arr[l:mid+1]
    rightArr=arr[mid+1:h+1]
    
    i=0
    j=0
    k=l
    while (i<len(leftArr) and j<len(rightArr)):
        if(leftArr[i]>rightArr[j]):
            arr[k]=rightArr[j]
            j+=1
            total+=len(leftArr) -i
        else:           
            arr[k]=leftArr[i]
            i+=1    
        k+=1          
    while(i<len(leftArr)):      
        arr[k]=leftArr[i]
        k+=1
        i+=1
        
    while(j<len(rightArr)):
        arr[k]=rightArr[j]
        j+=1
        k+=1
    return total
        

def MergeSort(arr,l,h):
    if l<h:
        mid=(l+h)//2
        count=MergeSort(arr,l,mid)+MergeSort(arr,mid+1,h)
        count+=Merge(arr,l,mid,h)
        return count
    return 0
        

def countInversions(arr):
    count=MergeSort(arr,0,len(arr)-1)
    return count
