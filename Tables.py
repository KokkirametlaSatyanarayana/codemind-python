a,b=map(int,input().split())
for i in range(1,b+1):
    if i%2!=0:
        print(a,end=' ')
        print('x',end=' ')
        print(i,end=' ')
        print('=',end=' ')
        print(a*i,end='')
        print()