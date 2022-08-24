a=int(input())
for i in range(a):
    m=input()
    if m=="".join(reversed(m)):
        if len(m)%2==0:
            print('YES','EVEN')
        else:
            print('YES','ODD')
    else:
        print('NO')