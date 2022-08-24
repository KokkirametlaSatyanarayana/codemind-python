a=int(input())
for i in range(a):
    k=input()
    count=0
    for i in range(len(k)):
        if ord(k[i])>=48 and ord(k[i])<=57:
            count+=1
    if count>0:
        print('Yes')
    else:
        print('No')
            
        