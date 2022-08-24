a=input()
m='z'
count=0
su=0
for i in range(len(a)):
    if a[i]==m:
        count+=1
    else:
        su+=1
if 2*count==su:
    print('Yes')
else:
    print('No')
    