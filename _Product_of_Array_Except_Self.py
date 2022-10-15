a=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    x=l[i]
    m=i
    f=1
    for i in range(len(l)):
        if x!=l[i] and i!=m:
            f*=l[i]
    print(f,end=" ")
            