f=int(input())
mem={}
while f>0:
    inp=input().split()
    mem[inp[0]]=True
    n=int(inp[1])
    for i in range(0,n):
        if inp[i+2] is not in mem:
            mem[inp[i+2]]=False
    f-=1
l=len(mem)
for i in range(0,l):
    
        
