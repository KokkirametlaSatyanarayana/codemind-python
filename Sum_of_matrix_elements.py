a=int(input())
b=int(input())
m=[]
for i in range(a):
    l=list(map(int,input().split()))
    m+=l
print(sum(m))