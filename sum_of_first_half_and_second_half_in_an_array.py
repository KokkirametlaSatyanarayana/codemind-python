a=int(input())
l=list(map(int,input().split()))
su=0
su1=0
for i in range(a//2):
    su=su+l[i]
for i in range(a//2,a):
    su1=su1+l[i]
print(su)
print(su1)