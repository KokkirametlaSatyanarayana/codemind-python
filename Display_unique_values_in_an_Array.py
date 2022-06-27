a=int(input())
l=list(map(int,input().split()))
count=0
su=0
for i in range(a):
    for j in range(a):
        if i!=j and l[i]==l[j]:
            count+=1
    if count==0:
        print(l[i],end=' ')
        su+=1
    count=0
if su==0:
    print('-1')
            


    
    
    
    
    