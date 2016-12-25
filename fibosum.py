mem={0:0,1:1}
def fib(n):
    if n%2==1:
        i=int((n+1)/2)
    else:
        i=int(n/2)
    if i in mem:
        x=mem[i]
    else:
        x=fib(i)
    if i-1 in mem:
        y=mem[i-1]
    else:
        y=fib(i-1)
    if n%2==1:
        mem[n]=((x*x)+(y*y))%1000000007
    else:
        mem[n]=((2*y+x)*x)%1000000007
    return mem[n]
t=int(input())
while t>0:
    t-=1
    x,y=input().split()
    x=int(x)
    y=int(y)
    print((fib(y+2)-fib(x+1))%1000000007)
