a=input()
l=list(map(int,input().split()))
count=0
for i in range(1,max(l)):
    if i not in l:
        print(i)
        count+=1
        break
if count==0:
    print(max(l)+1)
    