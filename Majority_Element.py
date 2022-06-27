a=int(input())
l=list(map(int,input().split()))
count=0
for i in range(a):
    for j in range(a):
        if l[i]==l[j]:
            count+=1
    if count>=((a//2)+1):
        print(l[i])
        break
    count=0


    
    
    
    
    