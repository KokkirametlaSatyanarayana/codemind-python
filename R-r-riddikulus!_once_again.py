a,b=map(int,input().split())
l=list(map(int,input().split()))
x=[]
y=[]
for i in range(b):
    x.append(l[i])
for i in range(b,a):
    y.append(l[i])
print(*(y+x))