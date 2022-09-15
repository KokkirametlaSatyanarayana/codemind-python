a=int(input())
for i in range(a):
    x=int(input())
    l=list(map(int,input().split()))
    m=sorted(l)
    if m==l:
        print('0')
    else:
        print(max(m)-min(m))
    