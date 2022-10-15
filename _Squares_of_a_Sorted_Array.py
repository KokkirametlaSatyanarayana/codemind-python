a=int(input())
l=list(map(int,input().split()))
x=[]
m=0
for i in range(len(l)):
    if l[i]<0:
        l[i]=-l[i]
x=sorted(l)
for i in range(len(x)):
    print(x[i]**2,end=" ")
    