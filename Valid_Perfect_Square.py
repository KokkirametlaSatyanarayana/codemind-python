a=int(input())
for i in range(a):
    x=int(input())
    count=0
    for i in range(1,x):
        if i*i==x:
            count+=1
    if count>=1:
        print(True)
    else:
        print(False)
            
    