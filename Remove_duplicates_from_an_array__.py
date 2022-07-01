a=int(input())
l=list(map(int,input().split()))
x=[]
for i in range(a):
    if l[i] not in x:
        x.append(l[i])
print(*x)
    
