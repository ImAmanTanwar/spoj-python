t=int(input())
oper={"+":1,"-":2,"/":3,"*":4,"/":5,"^":6}
def priority(x,y):
    if oper[x]>oper[y]:
        return True
    else:
        return False
while t>0:
    t-=1
    inp=input()
    l=len(inp)
    stk=[0]*100
    val=""
    top=0
    for i in range(0,l):
        if inp[i] in oper:
            if top>0 and stk[top-1]!="(":
                if priority(stk[top-1],inp[i]):
                    while top>0 and stk[top-1]!="(":
                        val+=stk[top-1]
                        top-=1
                else:
                    stk[top]=inp[i]
                    top+=1
            else:
                stk[top]=inp[i]
                top+=1
        elif inp[i]=="(":
            stk[top]=inp[i]
            top+=1
        elif inp[i]==")":
            while stk[top-1]!="(":
                val+=stk[top-1]
                top-=1
        else:
            val+=inp[i]
    print(val)
