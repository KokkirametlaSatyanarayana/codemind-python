a=int(input())
for i in range(a):
    x=int(input())
    m=[]
    l=[]
    b=0
    count=0
    temp=3
    while x>0:
        semp=x%10
        m=[]
        while len(m)<temp:
            remp=semp%2
            m.append(remp)
            semp=semp//2
        x=x//10
        l+=m
    for i in range(len(l)-1,-1,-1):
        if l[i]==0 and count==0:
            continue
        else:
            print(l[i],end="",)
            count+=1
    print()