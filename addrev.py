t=int(input())
while t>0:
    t-=1
    x,y=input().split()
    x=str(int(x))
    y=str(int(y))
    x=int(x[::-1])
    y=int(y[::-1])
    x+=y
    x=str(x)
    print(int(x[::-1]))
