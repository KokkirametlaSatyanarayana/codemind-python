a=int(input())
l=list(map(int,input().split()))
su=0
for i in range(a):
    for j in range(a):
        if(i!=j and l[i]==l[j]):
            su+=1
    if su>0:
        print(l[i])
        break
    su=0
    
    
    
    