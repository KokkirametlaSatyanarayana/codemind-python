a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
count=0
for i in range(len(l)):
    if l[i]%2==0:
        x.append(l[i])
    else:
        y.append(l[i])
if len(x)>len(y):
    for i in range(len(y)):
        print(x[i],y[i],end=" ")
        count+=1
    for i in range(count,len(x)):
        print(x[i],end=" ")
    if len(l)%2!=0:
        print("0")
if len(y)>len(x):
    for i in range(len(x)):
        print(x[i],y[i],end=" ")
        count+=1
    for i in range(count,len(y)):
        print(y[i],end=" ")
    if len(l)%2!=0:
        print("0")
elif len(x)==len(y):
    for i in range(len(x)):
        print(x[i],y[i],end=" ")
        
    
    
        