a=int(input())
l=list(map(int,input().split()))
count=0
s=0
x=[]
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count>=2 and l[i] not in x:
        s+=count//2
        x.append(l[i])
print(s)
        
