a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    print(*sorted(x+y))
    
    