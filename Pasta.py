a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=[]
count=0
for i in range(len(l2)):
        if l2[i] in l1 :
            if l2[i] not in x:
                count+=1
                x.append(l2[i])
if count==len(l2):
    print("Yes")
else:
    print("No")
                