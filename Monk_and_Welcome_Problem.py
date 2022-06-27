a=int(input())
l=list(map(int,input().split()))
b=list(map(int,input().split()))
su=0
for i in range(a):
    su+=l[i]+b[i]
    print(su,end=' ') 
    su=0
    
    
    