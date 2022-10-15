a=int(input())
b=(2**a)
for i in range(0,b):
    count=0
    x=i
    m=[]
    while count<a:
        temp=x%2
        m.append(temp)
        x=x//2
        count+=1
    for i in range(len(m)-1,-1,-1):
        print(m[i],end="")
    print()