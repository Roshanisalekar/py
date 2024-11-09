# factorial = 5! = 5*4*3*2*1 = 120
# factorial not use negative number
# condition

# num < 0  not valid
# num ==0  -> 1   answer 1 
# remember factorial = fact =1

#  using loop

num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
    i=i+1
    print(fact)



  #  step 2:
num=int(input("enter a number:"))
fact=1
if num<0:
    print("factorial 0 does not exist")
if num==0:
    print("factorial 0  is ",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i 
    print("the factorial is",fact)


    # USING RESURSION 
    #STEP : 3

def fact(a):
    if a==0 :
        return 1
    else:
        return (a) * fact(a-1)     # 5 * fact (4)
        
num=int(input("enter a number :"))
result=fact(num)
print(result)
