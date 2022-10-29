def prime(n):
    if n<2:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
    return 1
a=int(input())
count=0
for i in range(a):
    s=int(input())
    count=0
    x=1
    while count==0:
        if prime(s):
            print(s)
            break
        elif prime(s-x):
            print(s-x)
            break
        elif prime(s+x):
            print(s+x)
            break
        x+=1
        