a=int(input())
for i in range(a):
    x=int(input())
    l=list(map(int,input().split()))
    for i in range(1,x+1):
        if i not in l:
            print(i)