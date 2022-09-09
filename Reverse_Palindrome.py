def palindrome(n):
    count=0
    while n>0:
        temp=n%10
        count=count*10+temp
        n=n//10
    return count
a=int(input())
while a>0:
    x=a+palindrome(a)
    if palindrome(x)==x:
        print(x)
        break
    else:
        a=x