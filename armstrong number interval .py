lower=int(input("enter a  lower limit :"))
upper=int(input("enter a  upper limit :"))

for num in range (lower , upper +1 ):
    order = len(str(num))
    sum =0
    temp = num
while num>0 :
        digit=temp%10
        sum += digit ** order
        temp //=10
if num == sum :
        print("it is an armstrong number ")
else :
        print("it is not  an armstrong number ")