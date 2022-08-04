a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(a):
    if l[i]==0:
        x.append(l[i])
    else:
        y.append(l[i])
print(*(y+x))
    