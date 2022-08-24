a=input()
k=input()
count=0
for i in range(len(a)):
    if a[i]==k:
        count+=1
if count==0:
    print('-1')
else:
    print(count)
    