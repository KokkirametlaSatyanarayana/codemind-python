a=str(input())
count=0
for i in a:
    if ord(i)>=48 and ord(i)<=57:
        count+=1
if count>0:
    print('Contains',end=' ')
    print(count,end=' ')
    print('digit')
else:
    print("Doesn't contain",end=' ')
    print('digit')
        