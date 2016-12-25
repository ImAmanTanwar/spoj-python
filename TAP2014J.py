t=int(input())
nums=[]
for i in range(0,t):
    nums.append(int(input()))
mem=[]
n=t
def cal(t,count):
    if t==1:
        return
    while t>1:
        if count==nums[t-1]:
            mem.append(t-1)
            count=0
            cal(t-1,0)
            cal(t-1,count+1)
            return
        else:
            count+=1
    t-=1
cal(t,0)
l=len(mem)
while l>0:
    print(mem[l-1])
    l-=1
print(n)
