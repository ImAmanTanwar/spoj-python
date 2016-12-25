t=int(input())
while t>0:
    inp=input()
    l=len(inp)
    flag=0
    n=int(l/2)+1
    for i in range(0,n):
        if inp[i]!=inp[l-i-1]:
            flag=1
            print("NO")
            break
    if flag==0:
        print("YES")
    t-=1
