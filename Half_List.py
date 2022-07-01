a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
z=[]
for i in range(a//2):
    x.append(l[i])
for i in range(a//2,a):
    y.append(l[i])
for i in range(len(y)-1,-1,-1):
    z.append(y[i])
print(*(z+x))
