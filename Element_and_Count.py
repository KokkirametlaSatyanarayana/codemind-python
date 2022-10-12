a=int(input())
l=list(map(int,input().split()))
x=[]
count=0
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if l[i] not in x:
            print(l[i],count,end=" ")
            x.append(l[i])