a=int(input())
l=[]
while a>0:
    temp=a%2
    l.append(temp)
    a=a//2
for i in range(len(l)):
    if l[i]==0:
        l[i]=1
    elif l[i]==1:
        l[i]=0
x=len(l)
count=0
for i in range(len(l)):
    count+=(2**i)*l[i]
    x-=1
print(count)
    