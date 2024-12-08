string=input("enter a something :")
try:
    num=int(input("enter a number :"))
    print(string+num)
except(ValueError ,TypeError) as a:
    print(a)
print("thank you")