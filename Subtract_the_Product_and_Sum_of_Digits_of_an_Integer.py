n=int(input())
su=0
pro=1
while n>0:
    temp=n%10
    su=su+temp
    pro=pro*temp
    n=n//10
print(pro-su)