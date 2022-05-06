a=int(input())
count=0
for i in range(1,a):
    if i*i==a:
        count+=1 
if count==1:
    print('True')
else:
    print('False')
    
    