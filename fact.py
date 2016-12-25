t=int(input())
while t>0:
    num=int(input())
    val , i = 0 , 5
    while (num//i)!=0:
        val+=(num//i)
        i=i*5
    print(val)
    t-=1
