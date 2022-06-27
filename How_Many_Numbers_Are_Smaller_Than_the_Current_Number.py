a=int(input())
l=list(map(int,input().split()))
count=0
for i in range(a):
    for j in range(a):
        if j!=i and l[i]>l[j]:
            count+=1
    print(count,end=' ')
    count=0


    
    
    
    
    