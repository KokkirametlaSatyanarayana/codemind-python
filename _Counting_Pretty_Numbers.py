def pretty(n):
    if n%10==2 or n%10==3 or n%10==9:
        return 1
a=int(input())
for i in range(a):
    count=0
    m,n=map(int,input().split())
    for i in range(m,n+1):
        if pretty(i):
            count+=1
    print(count)