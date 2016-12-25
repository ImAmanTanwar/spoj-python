mem=[]
mem.append(2)
mem.append(3)
for i in range(5,100000):
    flag=0
    l=len(mem)
    for j in range(0,l):
        if i%mem[j]==0:
            flag=1
            break
    if flag==0:
        mem.append(i);
for i in range(0,len(mem)):
    print(mem[i])
