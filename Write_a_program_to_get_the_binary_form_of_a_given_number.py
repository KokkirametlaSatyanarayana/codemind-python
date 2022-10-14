a=int(input())
count=0
for i in range(a):
    x=int(input())
    m=[]
    while x>0:
        temp=x%2
        m.append(temp)
        x=x//2
    for i in range(len(m)-1,-1,-1):
        print(m[i],end="")
    print()
    