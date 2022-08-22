a=input()
count=0
x=[]
for i in range(len(a)):
    if (a[i]=='e' or a[i]=='a' or  a[i]=='i' or a[i]=='o' or a[i]=='u') or (a[i]=='E' or a[i]=='A' or  a[i]=='I' or a[i]=='O' or a[i]=='U'):
        if a[i] not in x:
            print(a[i],end=' ')
        x.append(a[i])
        count+=1
if count==0:
    print('-1')