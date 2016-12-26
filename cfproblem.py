def isPrime(num):
    n=int(num**(0.5))
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True
def minFactor(num):
    x,y=num,1
    minF=1+num
    m=int(num/2)
    for i in range(2,m+1):
        if num%i==0:
            if (num/i)+i<minF:
                minF=num/i + i
                x,y=num/i, i
    return x,y
def func(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    elif num==2:
        return 2
    elif isPrime(num):
        return 0
    else:
        x,y=minFactor(num)
        return func(x)+func(y)
inp=int(input())
print(func(inp))
