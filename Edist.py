t=int(input())
while t>0:
    t-=1
    src=input()
    dest=input()
    s_l=len(src)
    d_l=len(dest)
    if s_l==0:
        print(d_l)
    elif d_l==0:
        print(s_l)
    else:
        mem=[0]*((s_l+1)*(d_l+1))
        for i in range(0,s_l+1):
            mem[i*(s_l+1)]=i
        for i in range(0,d_l+1):
            mem[i]=i
        for i in range(1,s_l+1):
            for j in range(1,d_l+1):
                mem[i*(s_l+1)+j]=1+min(i*(s_l+1)+j-1,(i-1)*(s_l+1)+j,(i-1)*(s_l+1)+j-1)
        print(mem[s_l*d_l])
                
    
