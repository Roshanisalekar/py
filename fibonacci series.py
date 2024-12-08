# using fibonacci series

# 0+1+1+2+3+5+8  this is fibonacci series
a=0
b=1
num=int(input("enter a fibonacci series num :"))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
for i in range(2,num+1):
    c=a+b
    a=b
    b=c
    print(c)