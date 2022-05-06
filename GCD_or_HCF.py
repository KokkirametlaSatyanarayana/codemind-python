a,b=map(int,input().split())
a<b
for i in range(1,b+1):
    if a%i==0 and b%i==0:
        temp=i
print(temp)
