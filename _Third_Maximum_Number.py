a=int(input())
l=list(map(int,input().split()))
x=set(l)
y=sorted(list(x))
if a<=2:
    print(l[-1])
else:
    print(y[-3])
    