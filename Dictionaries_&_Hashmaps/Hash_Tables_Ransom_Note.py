def checkMagazine(magazine, note):
    # Write your code here
    # print(magazine,note)
    magazineDict={}
    noteDict={}
    for i in magazine:
        if i in magazineDict:
            magazineDict[i]+=1
        else:
            magazineDict[i]=1
    for i in note:
        if i in magazineDict:
            if magazineDict[i]>0:
                magazineDict[i]-=1
                continue
            print("No")
            return
        print("No")
        return                
    print("Yes")
