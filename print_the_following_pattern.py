a=int(input())
for i in range(a,0,-1):
    b=chr(64+i)
    for j in range(1,i+1):
        print(b,end=" ")
    print()