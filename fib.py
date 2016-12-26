mem={0:0,1:1}
def fib(n):
    if n%2==1:
        i=(n+1)//2
    else:
        i=n//2
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
print(fib(t))
