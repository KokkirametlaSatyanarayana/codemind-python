a=int(input())
flag=0
for i in range(1,a):
    if i*(i+1)==a:
        print('YES')
        break
else:
    print('NO')