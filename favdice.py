t=int(input())
while t>0:
    inp=int(input())
    num=0
    for i in range(1,inp+1):
        num+=inp*(1/i)
    print("{0:.2f}".format(num))
    t-=1
