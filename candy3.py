t=int(input())
while t>0:
    t-=1
    input()
    n=int(input())
    s=0
    for i in range(0,n):
        s+=int(input())
    if s%n==0:
        print("YES")
    else:
        print("NO")
