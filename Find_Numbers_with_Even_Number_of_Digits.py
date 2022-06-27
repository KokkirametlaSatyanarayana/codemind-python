def count(n):
    su=0
    while n>0:
        n=n//10
        su+=1
    return su
a=int(input())
l=list(map(int,input().split()))
b=0
for i in range(a):
    if count(l[i])%2==0:
        b+=1
print(b)


    
    
    
    
    