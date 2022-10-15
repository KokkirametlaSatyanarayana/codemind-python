x=int(input())
m=[]
l=[]
count=0
temp=3
while x>0:
    m=[]
    semp=x%10
    while count<temp:
        remp=semp%2
        m.append(remp)
        semp=semp//2
        count+=1
    l+=m
    x=x//10
    count=0
count=0
for i in range(len(l)-1,-1,-1):
    if l[i]==0 and count==0:
        continue
    else:
        print(l[i],end="")
        count+=1
        
        