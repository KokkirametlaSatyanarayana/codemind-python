a=int(input())
b="0000"
c="0001"
d="0010"
e="0011"
f="0100"
g="0101"
h="0110"
i="0111"
j="1000"
k="1001"
l="1010"
s="1011"
n="1100"
o="1101"
p="1110"
q="1111"
for i in range(a):
    x=input()
    m=""
    for i in range(len(x)):
        if x[i]=="0":
            m+=b
        if x[i]=="1":
            m+=c
        if x[i]=="2":
            m+=d
        if x[i]=="3":
            m+=e
        if x[i]=="4":
            m+=f
        if x[i]=="5":
            m+=g
        if x[i]=="6":
            m+=h
        if x[i]=="7":
            m+=i
        if x[i]=="8":
            m+=j
        if x[i]=="9":
            m+=k
        if x[i]=="A":
            m+=l
        if x[i]=="B":
            m+=s
        if x[i]=="C":
            m+=n
        if x[i]=="D":
            m+=o
        if x[i]=="E":
            m+=p
        if x[i]=="F":
            m+=q
    print(m)
        