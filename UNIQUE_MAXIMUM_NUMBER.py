a=int(input())
l=list(map(int,input().split()))
x=set(l)
y=list(l)
su=0
z=[]
count=0
for i in range(len(y)):
    for j in range(len(l)):
        if y[i]==l[j]:
            count+=1
    if count==1:
        z.append(y[i])
        su+=1
    count=0
if su==0:
    print('-1')
else:
    print(max(z))
        
        
        
        
        
        

    