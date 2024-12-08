# using third variable
x=12
y=14
temp=x
print("temp:",temp)
x=y
print("x is :",x)
y=temp
print("y is :", y)


#without third variable
x=12
y=14
x,y=y,x
print("the value of x:",x)
print("the value of y:",y)