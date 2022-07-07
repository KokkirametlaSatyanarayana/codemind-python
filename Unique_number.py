a=int(input())
k=a
l=[]
count=0
flag=0
while a>0:
    temp=a%10
    l.append(temp)
    a=a//10
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]==l[j] and i!=j:
            count+=1
    if count==1:
        flag+=1
        break
    count=0
if flag==1:
    print('Not Unique Number')
else:
    print('Unique Number')
            
        