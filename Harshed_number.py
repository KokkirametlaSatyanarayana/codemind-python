a=int(input())
m=a
su=0
while a>0:
    temp=a%10
    su=su+temp
    a=a//10
if m%su==0:
    print(True)
else:
    print(False)