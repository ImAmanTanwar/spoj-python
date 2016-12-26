t=int(input())
while t>0:
    t-=1
    num,index=input().split()
    num=int(num)
    index=int(index)
    if index==0 and num!=0:
        print("1")
        continue
    num=num%10
    if num==0 or num==1 or num==5 or num==6:
        print(num)
        continue
    mem=[]
    mem.append(num)
    num=(num*num)%10
    while num!=mem[0]:
        mem.append(num)
        num=(num*mem[0])%10
    l=len(mem)
    print(mem[(index%l)-1]) 
