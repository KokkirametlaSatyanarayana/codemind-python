a,b,c=map(int,input().split())
d=(a+b+c)/2
x=d*(d-a)*(d-b)*(d-c)
import math
print(format(math.sqrt(x),".2f"))
