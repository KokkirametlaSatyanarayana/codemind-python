a=str(input())
count4=0
count1=0
count2=0
count3=0
count5=0
for i in a:
    if ord(i)==32:
        count1+=1
    elif ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85 or  ord(i)==97 or ord(i)==101 or ord(i)==105 or ord(i)==111 or ord(i)==117:
        count2+=1
    elif ord(i)>=65 and ord(i)<=90  and  ord(i)!=65 and ord(i)!=69 and ord(i)!=73 and ord(i)!=79 and ord(i)!=85:
        count3+=1
    elif ord(i)>=97 and ord(i)<=122  and  ord(i)!=97 and ord(i)!=101 and ord(i)!=105 and ord(i)!=111 and ord(i)!=117:
        count4+=1
    elif ord(i)==32:
        count5+=1
print(count1+1)

        