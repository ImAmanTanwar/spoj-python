t=int(input())
def find(a,n,j):
    p=-1
    for i in range(0,n):
        if a[i]==j:
            p=i
            break
    return p
while t>0:
    t-=1
    n=int(input())
    nums=[0] * n
    mem=[0]*n
    temp=[0]*n
    inp=input().split()
    for i in range(0,n):
        nums[i]=int(inp[i])
        mem[i]=nums[i]
    mem.sort()
    for i in range(0,n):
        temp[find(mem,n,nums[i])]=i
    c,p=0,1
    for i in range(1,n):
        if temp[i]>temp[i-1]:
            p+=1
        elif p>c:
            c=p
            p=1
    if p>c:
        c=p
    print(n-c)
