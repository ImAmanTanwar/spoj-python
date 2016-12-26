t=int(input())
while t>0:
    s=""
    n,x,y=input().split()
    n,x,y=int(n),int(x),int(y)
    i=1
    while i*x<n:
        if (i*x)%y!=0:
            s+=str(i*x)+" "
        i+=1
    print(s)
    t-=1
