# using for loop
print("the number divisible by 13 number:")
for i in range(1,150):
    if i%13==0:
        print(i)
       
        
# using lambda function and filter
l=[39,53,78,130,87,91,41,47]
result=list(filter(lambda x : x %13==0,l))
print(result)