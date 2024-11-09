print("~~~~~MINI CALCULATOR~~~~~")

num1=int(input("enter a first number :"))
num2=int(input("enter a second number :"))

print("press 1 for addition \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division \n")
choice=int(input("enter your choice :"))
if choice == 1 :
    print(num1 + num2)
elif choice == 2 :
    print(num1  - num2)
elif choice == 3 :
    print(num1  * num2)
elif choice == 4 :
    print(num1 / num2)
else :
    print("invalid choice")