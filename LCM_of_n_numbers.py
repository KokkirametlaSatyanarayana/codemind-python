a=int(input())
l=list(map(int,input().split()))
x=1
for i in range(a):
    x*=l[i]
for i in range(l[a-1],x+1):
    m=i
    count=0
    for i in range(len(l)):
        if m%l[i]==0:
            count+=1
    if count==len(l):
        print(m)
        break
        
        
        
    
    