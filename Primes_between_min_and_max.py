def prime(n):
    if n<2:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return 0
    return 1
a=int(input())
l=list(map(int,input().split()))
count=0
m=min(l)
n=max(l)
for i in range(len(l)):
    if l[i]==m:
        m=i
        count+=1
    if l[i]==n:
        n=i
        count+=1
    if count==2:
        break
count=0
for i in range(len(l)):
    if (i<=m and i>=n) or (i<=n and i>=m):
        if prime(l[i]):
            count+=1
print(count)