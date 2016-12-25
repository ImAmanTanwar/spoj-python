t=int(input())
while t>0:
    t-=1
    x,y=input().split()
    x=int(x)
    y=int(y)
    count=0
    if y<x:
        temp=x
        x=y
        y=temp
    if x==0 or y==0:
        print("0")
        continue
    elif y>=2*x:
        print(x)
        continue
    while x!=y:
        count+=1
        x-=1
        y-=2
    while x>0 and y>0:
        if x==1 and y==1:
            break
        m=(count%2)+1
        x-=m
        y-=((m%2)+1)
        count+=1
    print(count)
