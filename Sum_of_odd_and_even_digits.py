a=int(input())
l=list(map(int,input().split()))
count=0
su=0
for i in range(a):
        if i%2==0:
            count+=l[i]
        else:
            su+=l[i]
if count-su==0:
    print('YES')
else:
    print("NO")
            


    
    
    
    
    