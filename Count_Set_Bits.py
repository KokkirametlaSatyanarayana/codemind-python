a=int(input())
for i in range(a):
    x=int(input())
    co=0
    l=[]
    while x>0:
        temp=x%2
        l.append(temp)
        x=x//2
    for i in range(len(l)):
        if l[i]==1:
            co+=1
    print(co)