def su(n):
    count=0
    while n>0:
        temp=n%10
        count+=temp**2
        n=n//10
    return count
a=int(input())
count=0
while a>0:
    if su(a)==1 or su(a)==7:
        count+=1
        break
    elif su(a)%10==su(a):
        break
    else:
        a=su(a)
if count==1:
    print(True)
else:
    print(False)