a=int(input())
count=0
l=list(map(int,input().split()))
for i in range(len(l)-1):
    if (l[i]%2==0 and l[i+1]%2!=0) or (l[i]%2!=0 and l[i+1]%2==0) or(l[i]%2==0 and l[i+1]%2==0):
        count+=1
if count==a-1:
    print("YES")
else:
    print("NO")
    
    