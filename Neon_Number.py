n=int(input())
su=0
m=n*n
while m>0:
    temp=m%10
    su=su+temp
    m=m//10
if su==n:
    print('Neon Number')
else:
    print('Not Neon Number')