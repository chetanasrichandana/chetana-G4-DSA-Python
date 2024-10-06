def anagram:
    arr=["eat", "tea", "tan", "ate", "nat", "bat"]
    def helper(str1,str2)->bool:
        if len(str1)!=len(str2):
            return False
        d={}
        for i in str1:
            d[i]=d.get(i,0)+1

        for i in str2:
            d[i]=d.get(i,0)-1

        for i in d:
            if d[i]!=0:
                return False
        return True
    res=[]
    i=0
    while(i<len(arr)):
        temp=[]
        j=i+1
        while(j<len(arr)):
            ans=helper(arr[i],arr[j])
            if ans:
                temp.append(arr[j])
                arr.remove(arr[j])
            j+=1
        
        temp.insert(0,arr[i])
        res.append(temp)
        i+=1
    
    print(res)
