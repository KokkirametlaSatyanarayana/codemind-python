a=int(input())
count=0
l=[]
while a>0:
    temp=a%10
    l.append(temp)
    a=a//10
for i in range(len(l)-1,-1,-1):
    if l[i]==6:
        l[i]=9
        break
for i in range(len(l)-1,-1,-1):
    print(l[i],end='')
    
    
    
    