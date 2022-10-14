a=int(input())
for i in range(a):
    x=int(input())
    count=0
    s=0
    while x>0:
        temp=x%10
        count+=(2**s)*temp
        x=x//10
        s+=1
    print(count)
        
        