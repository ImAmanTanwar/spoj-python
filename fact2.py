t=int(input())
mem=[None]*100
mem[0]=1
for i in range(2,101):
    mem[i-1]=i*mem[i-2]
while t>0:
    inp=int(input())
    print(mem[inp-1])
    t-=1
