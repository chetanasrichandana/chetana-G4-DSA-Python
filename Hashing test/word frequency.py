def word_frequency:
    str1="Hello, hello! How are you? Are you there?"
    s=""
    for i in str1:
        if i>='a' and i<='z' or i>='A' and i<='Z':
            s+=i
        elif i==" ":
            s+=" "
        else:
            pass
    s=s.lower()
    l=s.split(" ")
    print(l)
    d={}
    for i in l:
        d[i]=d.get(i,0)+1
    print(d)
