def fib(n,m,mem):
    if n%2==1:
        i=int((n+1)/2)
    else:
        i=int(n/2)
    if i in mem:
        x=mem[i]
    else:
        x=fib(i,m,mem)
    if i-1 in mem:
        y=mem[i-1]
    else:
        y=fib(i-1,m,mem)
    if n%2==1:
        mem[n]=((x*x)+(y*y))%m
    else:
        mem[n]=((2*y+x)*x)%m
    return mem[n]
t=int(input())
while t>0:
    mem={0:0,1:1}
    t-=1
    x,y=input().split()
    x=int(x)
    y=int(y)
    f=(((2*(fib(x+2,y,mem)-1)))-x)%y
    print(f) 
