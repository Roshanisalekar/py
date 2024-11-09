"""armstrong number means is 153 exactly 153 this armstrong number
153=(1*1*1)+(5*5*5)+(3*3*3)
   =1+125+27
   =153  this is  armstrong number

   53=(5*5)+(3*3)
     =25+9
     =34  this is not armstrong number"""


num= int(input("enter a number :"))
sum=0
temp=num
while temp>0:
    digit = temp%10
    cube = digit ** 3    # only 3 digit number 
    sum = sum + cube
    temp //=10
if num==sum :
    print("it is an armstrong number")
else:
    print("it is  not an armstrong number")



    # 4 digit 

    num= int(input("enter a number :"))
order = len(str(num))
sum=0
temp=num
while temp>0:
    digit = temp%10
    cube = digit ** order   # 4,5,6 digit number and soon  number
    sum = sum + cube
    temp //=10
if num==sum :
    print("it is an armstrong number")
else:
    print("it is  not an armstrong number")