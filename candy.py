while True:
    n=int(input())
    if n==-1:
        break
    arr=[0]*n
    s=avg=val=0
    for i in range(0,n):
        arr[i]=int(input())
        s+=arr[i]
    if s%n!=0:
        print("-1")
        continue
    avg=s//n
    for i in range(0,n):
        if arr[i]<avg:
            val+=avg-arr[i]
    print(val)
