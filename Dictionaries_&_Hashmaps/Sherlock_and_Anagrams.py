def sherlockAndAnagrams(s):
    # Write your code here
    l=len(s)
    count=0
    for i in range(1,l):
        dic={}
        for j in range(l-i+1):
            t=str(sorted(s[j:j+i]))
            # print("t",t)
            if t not in dic:
                dic[t]=1
            else:
                dic[t]+=1
        # print(dic)
        for j in dic:
            count+=((dic[j])*(dic[j]-1))//2
        # print(count)
    return(count)
