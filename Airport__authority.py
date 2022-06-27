a=int(input())
su=0
k=[]
for i in range(a):
    k.append(int(input()))
b=int(input())
for i in range(len(k)):
    if k[i]<=b:
        su+=1
    else:
        su+=2
print(su)
    
