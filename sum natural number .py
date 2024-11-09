num = int(input("enter a number :"))
if num < 0:
    print("please enter  positive a number ")
else:
    sum=0
    while num>0:
         sum=sum+num
         num=num-1
    print(sum)

