a=input()
k=input()
count=0
for i in range(len(a)):
    if a[i]==k:
        print(True)
        print(i)
        count+=1
        break
if count==0:
    print(False)