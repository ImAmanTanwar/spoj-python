t=int(input())
while t>0:
    t-=1
    s=0
    n=int(input())
    inp_m=input().split()
    inp_f=input().split()
    male=[]
    female=[]
    for i in range(0,n):
        male.append(int(inp_m[i]))
        female.append(int(inp_f[i]))
    male.sort()
    female.sort()
    for i in range(0,n):
        s+=male[i]*female[i]
    print(s)
