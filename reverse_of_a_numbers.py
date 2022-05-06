a=int(input())
rev=0
while a>0:
    temp=a%10
    rev=rev*10+temp
    a=a//10
print(rev)