a=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    x=l[i]
    m=i
    count=0
    for i in range(m+1,len(l)):
        if l[i]>x:
            print(i-m,end=" ")
            count+=1
            break
    if count==0:
        print(0,end=" ")
