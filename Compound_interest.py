p,r,t=map(int,input().split())
x=(1+(r/100))**t
print(format(x*p,".2f"))