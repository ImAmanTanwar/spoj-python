while True:
    inp=input()
    if inp=='0':
        break
    l=len(inp)
    mem=[0]*5050
    mem[0]=mem[1]=1
    for i in range(1,l):
        if inp[i]!='0':
            mem[i+1]=mem[i]
        num=int(inp[i-1:i+1])
        if num>=10 and num<=26:
            mem[i+1]+=mem[i-1]
    print(mem[l])
