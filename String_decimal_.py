m=int(input())
for i in range(m):
    a=input()
    count=0
    for i in range(len(a)):
        if ord(a[i])>=48 and ord(a[i])<=57:
            count+=1
    if count==len(a):
        print(True)
    else:
        print(False)