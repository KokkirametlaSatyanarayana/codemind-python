a=int(input())
b=int(input())
sum1=0
sum2=0
for i in range(1,a):
    if a%i==0:
        sum1=sum1+i
for i in range(1,b):
    if b%i==0:
        sum2=sum2+i
if a==sum2 and b==sum1:
    print('Amicable')
else:
    print('Not Amicable')
    